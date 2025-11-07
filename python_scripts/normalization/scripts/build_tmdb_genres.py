"""
build_tmdb_genres.py

Build a normalized TMDB genre dictionary (movie + tv) for FindMyFlick.

- Reads TMDB_API_KEY from env or repo root .env (no extra deps)
- Fetches:
    /genre/movie/list
    /genre/tv/list
  (defaults to language=en-US, but configurable)

Outputs: python_scripts/normalization/data/tmdb/genres.json

Structure:
{
  "source": "tmdb",
  "language": "en-US",
  "generatedAt": "...Z",
  "genres": {
    "movie": [ { "id": 28, "name": "Action", "slug": "action" }, ... ],
    "tv":    [ { "id": 10759, "name": "Action & Adventure", "slug": "action-adventure" }, ... ]
  },
  "byId": {
    "movie:28":   { "id": 28, "mediaType": "movie", "name": "Action", "slug": "action" },
    "tv:10759":   { "id": 10759, "mediaType": "tv", "name": "Action & Adventure", "slug": "action-adventure" }
  },
  "union": {
    "action": { "name": "Action", "movieId": 28, "tvId": null },
    "action-adventure": { "name": "Action & Adventure", "movieId": null, "tvId": 10759 },
    ...
  }
}
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
import argparse
import requests

API = "https://api.themoviedb.org/3"
HEADERS = {"Accept": "application/json"}

# ---------- tiny .env loader (same pattern as providers script) ----------
def load_dotenv_from_repo_root():
    if os.getenv("TMDB_API_KEY"):
        return
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
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s

def get(api_path, api_key, params=None):
    params = dict(params or {})
    params["api_key"] = api_key
    r = requests.get(f"{API}{api_path}", params=params, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.json()

def fetch_genres(api_key, language="en-US"):
    movie = get("/genre/movie/list", api_key, {"language": language}).get("genres", [])
    tv    = get("/genre/tv/list",    api_key, {"language": language}).get("genres", [])
    # Normalize with slugs
    movie_norm = [{"id": g["id"], "name": g["name"], "slug": slugify(g["name"])} for g in movie if "id" in g and "name" in g]
    tv_norm    = [{"id": g["id"], "name": g["name"], "slug": slugify(g["name"])} for g in tv    if "id" in g and "name" in g]
    return movie_norm, tv_norm

def build_union(movie_genres, tv_genres):
    """
    Build a union keyed by slug. When the same slug appears in both sets,
    we keep both IDs. If a slug exists in only one set, the other ID is null.
    """
    union = {}
    for g in movie_genres:
        union[g["slug"]] = {"name": g["name"], "movieId": g["id"], "tvId": None}
    for g in tv_genres:
        if g["slug"] in union:
            # If names differ slightly (e.g., "Action" vs "Action & Adventure"), prefer the TV name for display if movie name missing
            union[g["slug"]]["tvId"] = g["id"]
            # Keep the first name we encountered; optionally you could reconcile here if needed.
        else:
            union[g["slug"]] = {"name": g["name"], "movieId": None, "tvId": g["id"]}
    return union

def build_by_id(movie_genres, tv_genres):
    by_id = {}
    for g in movie_genres:
        by_id[f"movie:{g['id']}"] = {"id": g["id"], "mediaType": "movie", "name": g["name"], "slug": g["slug"]}
    for g in tv_genres:
        by_id[f"tv:{g['id']}"] = {"id": g["id"], "mediaType": "tv", "name": g["name"], "slug": g["slug"]}
    return by_id

def main():
    load_dotenv_from_repo_root()
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        raise SystemExit("TMDB_API_KEY not found. Add it to your root .env or environment.")

    ap = argparse.ArgumentParser()
    ap.add_argument("--language", default="en-US", help="TMDB language code (default: en-US)")
    ap.add_argument("--output", default="python_scripts/normalization/data/tmdb/genres.json", help="Output JSON path")
    args = ap.parse_args()

    movie_genres, tv_genres = fetch_genres(api_key, language=args.language)
    union = build_union(movie_genres, tv_genres)
    by_id = build_by_id(movie_genres, tv_genres)

    out = {
        "source": "tmdb",
        "language": args.language,
        "generatedAt": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "genres": {
            "movie": movie_genres,
            "tv": tv_genres
        },
        "byId": by_id,
        "union": union
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out_path}")
    print(f"  movie genres: {len(movie_genres)}")
    print(f"  tv genres:    {len(tv_genres)}")
    print(f"  union keys:   {len(union)}")

if __name__ == "__main__":
    main()