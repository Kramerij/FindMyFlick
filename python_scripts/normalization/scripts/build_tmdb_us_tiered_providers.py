"""
build_tmdb_us_tiered_providers.py

Build a US-tiered provider list from TMDB, matching your DTDD flow.

Tiers (always present as separate lists):
- subscription    <- TMDB 'flatrate'
- free_with_ads   <- TMDB 'free' + 'ads'
- rent            <- TMDB 'rent'
- buy             <- TMDB 'buy'

How it works (no pre-saved JSON required):
1) Reads TMDB_API_KEY from the environment, and if missing, from a .env at the repo root.
2) Seeds a set of movie/TV IDs from TMDB (trending + popular) to discover providers.
3) For each id, calls /{type}/{id}/watch/providers and aggregates US providers by monetization bucket.
4) Optionally enriches provider name/logo/priority from /watch/providers/movie|tv (US).
5) Writes a single JSON to python_scripts/normalization/data/tmdb/services_us_tiered.json

Standard library + requests only.
"""

import os
import json
import re
import time
from pathlib import Path
from datetime import datetime
import argparse
import requests

API = "https://api.themoviedb.org/3"
HEADERS = {"Accept": "application/json"}
SLEEP_SECS = 0.2
DEFAULT_SEED_PAGES = 3

# ---------- small .env loader (no extra deps) ----------
def load_dotenv_from_repo_root():
    """
    If TMDB_API_KEY is not in os.environ, try to read a .env at the repository root.
    Root is inferred as the first parent directory that contains a .git folder,
    falling back to the current working directory.
    """
    if os.getenv("TMDB_API_KEY"):
        return
    # find repo root by walking up until .git or stop at filesystem root
    p = Path.cwd()
    root = None
    for ancestor in [p] + list(p.parents):
        if (ancestor / ".git").exists() or (ancestor / ".env").exists():
            root = ancestor
            break
    if not root:
        return
    env_file = root / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        os.environ.setdefault(k, v)

# ---------- helpers ----------
def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s

def req(path, params=None, api_key=None):
    params = dict(params or {})
    params["api_key"] = api_key
    r = requests.get(f"{API}{path}", params=params, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.json()

def seed_ids(api_key, pages=DEFAULT_SEED_PAGES):
    ids = {"movie": set(), "tv": set()}
    for media_type in ("movie", "tv"):
        for page in range(1, pages + 1):
            data = req(f"/trending/{media_type}/week", {"page": page}, api_key)
            for item in data.get("results", []):
                if item.get("id"):
                    ids[media_type].add(item["id"])
            time.sleep(SLEEP_SECS)
    for media_type in ("movie", "tv"):
        for page in range(1, pages + 1):
            data = req(f"/{media_type}/popular", {"page": page}, api_key)
            for item in data.get("results", []):
                if item.get("id"):
                    ids[media_type].add(item["id"])
            time.sleep(SLEEP_SECS)
    return ids

def harvest_per_title_providers(api_key, ids_by_type):
    tiers = {
        "subscription": {},    # flatrate
        "free_with_ads": {},   # free + ads
        "rent": {},            # rent
        "buy": {},             # buy
    }
    mapping = {
        "flatrate": "subscription",
        "free": "free_with_ads",
        "ads": "free_with_ads",
        "rent": "rent",
        "buy": "buy",
    }
    for media_type, idset in ids_by_type.items():
        for mid in idset:
            data = req(f"/{media_type}/{mid}/watch/providers", {}, api_key)
            us = ((data.get("results") or {}).get("US")) or {}
            for bucket, tier in mapping.items():
                arr = us.get(bucket)
                if not isinstance(arr, list):
                    continue
                for p in arr:
                    pid = p.get("provider_id")
                    name = p.get("provider_name")
                    if not pid or not name:
                        continue
                    tiers[tier][pid] = {
                        "serviceId": pid,
                        "name": name,
                        "slug": slugify(name),
                        "logoPath": p.get("logo_path"),
                        "displayPriority": p.get("display_priority"),
                    }
            time.sleep(SLEEP_SECS)
    return tiers

def enrich_from_catalog(api_key, tiers):
    def fetch_catalog(kind):
        data = req(f"/watch/providers/{kind}", {"watch_region": "US"}, api_key)
        out = {}
        for p in data.get("results", []):
            pid = p.get("provider_id")
            name = p.get("provider_name")
            if not pid or not name:
                continue
            out[pid] = {
                "serviceId": pid,
                "name": name,
                "slug": slugify(name),
                "logoPath": p.get("logo_path"),
                "displayPriority": p.get("display_priority"),
            }
        return out

    movie_cat = fetch_catalog("movie")
    time.sleep(SLEEP_SECS)
    tv_cat = fetch_catalog("tv")
    catalog = {**movie_cat, **{k: v for k, v in tv_cat.items() if k not in movie_cat}}

    for tier_name, provs in tiers.items():
        for pid, item in list(provs.items()):
            enrich = catalog.get(pid)
            if not enrich:
                continue
            item["name"] = item.get("name") or enrich.get("name")
            item["slug"] = item.get("slug") or enrich.get("slug")
            if item.get("logoPath") is None:
                item["logoPath"] = enrich.get("logoPath")
            if item.get("displayPriority") is None:
                item["displayPriority"] = enrich.get("displayPriority")
            tiers[tier_name][pid] = item
    return tiers

def main():
    load_dotenv_from_repo_root()
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        raise SystemExit("TMDB_API_KEY not found. Add it to your root .env or environment.")

    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, default=DEFAULT_SEED_PAGES, help="Pages of trending+popular per media type to seed IDs")
    ap.add_argument("--output", default="python_scripts/normalization/data/tmdb/services_us_tiered.json", help="Output JSON path")
    args = ap.parse_args()

    ids_by_type = seed_ids(api_key, pages=args.pages)
    tiers = harvest_per_title_providers(api_key, ids_by_type)
    tiers = enrich_from_catalog(api_key, tiers)

    def sorted_list(d):
        return sorted(
            d.values(),
            key=lambda x: (9999 if x.get("displayPriority") is None else x["displayPriority"], x.get("name") or "")
        )

    out = {
        "region": "US",
        "source": "tmdb",
        "generatedAt": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "tiers": {
            "subscription":   sorted_list(tiers["subscription"]),
            "free_with_ads":  sorted_list(tiers["free_with_ads"]),
            "rent":           sorted_list(tiers["rent"]),
            "buy":            sorted_list(tiers["buy"])
        }
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out_path}")
    for k, v in out["tiers"].items():
        print(f"  {k}: {len(v)} providers")

if __name__ == "__main__":
    main()