"""
schema_dtdd_topics_catalog.py
-----------------------------

Purpose:
    Build a catalog of DoesTheDogDie topics by sampling a diverse list of titles
    (no TMDB dependency). For each title:
      1) /dddsearch?q={title} -> first item id
      2) /media/{itemId} -> topicItemStats
    Aggregate unique topics (id, name, description), count how many titles include
    each topic (yesSum > 0), and keep a few example titles.

Outputs (written to python_scripts/assets/):
    - dtdd_topics_catalog.csv
    - dtdd_topics_catalog.md
    - dtdd_topics_catalog.json

Usage (from repo root):
    python -m python_scripts.dtdd.schema_dtdd_topics_catalog

Requirements:
    - .env with DTDD_API_KEY
    - requests, python-dotenv
"""

import os
import csv
import time
import json
from collections import defaultdict

from python_scripts.shared.schema_utils import load_api_key, fetch_json

# Diverse seed list: mix of genres, eras, and languages (US-available is fine;
# DTDD is crowd-sourced, so broader variety yields broader topics)
SEED_TITLES = [
    # Horror / thriller (US / foreign)
    "Fight Club", "The Exorcist", "Hereditary", "Talk to Me",
    "Train to Busan", "Ringu", "The Babadook", "Get Out",

    # Comedy / satire (older/newer)
    "Blazing Saddles", "Airplane!", "Superbad", "Mean Girls",

    # Drama / prestige
    "The Godfather", "Moonlight", "Manchester by the Sea", "The Social Network",

    # Romance / rom-com
    "La La Land", "Pride & Prejudice", "The Notebook", "Crazy Rich Asians",

    # Action / adventure
    "Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator",

    # Documentary
    "Free Solo", "Blackfish", "The Cove", "Won't You Be My Neighbor?",

    # Animation / family
    "Toy Story", "Inside Out", "Spirited Away", "Coco",

    # Crime / legal / justice-themes
    "12 Angry Men", "Mystic River", "Zodiac", "Prisoners",

    # War / historical
    "Schindler's List", "Saving Private Ryan", "1917", "Dunkirk",

    # Social issues / racism themes
    "Mississippi Burning", "Do the Right Thing", "12 Years a Slave", "Selma",

    # International drama
    "Parasite", "Amélie", "Cinema Paradiso", "Pan's Labyrinth",

    # Horror classics with pet harm themes
    "Halloween", "Pet Sematary", "The Thing", "The Fly",
]

DTDD_SEARCH = "https://api.doesthedogdie.com/dddsearch"
DTDD_MEDIA  = "https://api.doesthedogdie.com/media/{item_id}"

SLEEP_BETWEEN_REQUESTS = 0.15  # be polite


def resolve_dtdd_item_id_by_title(title: str, api_key: str) -> tuple[str | None, str | None]:
    """Return (item_id, matched_title) or (None, None) using DTDD title search."""
    headers = {"Accept": "application/json", "x-api-key": api_key}
    params = {"q": title}
    try:
        data = fetch_json(DTDD_SEARCH, params=params, headers=headers)
    except Exception as e:
        print(f"  ! search failed for {title!r}: {e}")
        return None, None
    items = (data or {}).get("items") or []
    if not items:
        return None, None
    first = items[0] or {}
    return first.get("id"), first.get("name") or title


def fetch_topic_item_stats(item_id: str, api_key: str) -> list:
    """Return topicItemStats (may be empty) from DTDD /media/{item_id}."""
    headers = {"Accept": "application/json", "x-api-key": api_key}
    url = DTDD_MEDIA.format(item_id=item_id)
    data = fetch_json(url, headers=headers)
    return (data or {}).get("topicItemStats") or []


def main():
    api_key = load_api_key("DTDD_API_KEY")

    print("Building DoesTheDogDie topics catalog from sampled titles...\n")

    # Aggregation structures
    topics = {}  # topic_id -> {"name": ..., "description": ...}
    hit_counts = defaultdict(int)  # topic_id -> number of titles where topic has yesSum > 0
    examples = defaultdict(set)    # topic_id -> set of example titles

    processed = 0
    resolved = 0
    skipped = 0

    for title in SEED_TITLES:
        processed += 1
        print(f"[{processed:02d}/{len(SEED_TITLES)}] Resolving: {title!r}")

        item_id, matched = resolve_dtdd_item_id_by_title(title, api_key)
        if not item_id:
            print("   -> no DTDD item found; skipped")
            skipped += 1
            time.sleep(SLEEP_BETWEEN_REQUESTS)
            continue

        resolved += 1
        stats = fetch_topic_item_stats(item_id, api_key)

        # Consider a topic a "hit" for a title only if yesSum > 0
        seen_this_title = set()
        for t in stats:
            if not isinstance(t, dict):
                continue
            yes_sum = t.get("yesSum") or 0
            if yes_sum <= 0:
                continue

            topic = t.get("topic") or {}
            tid = topic.get("id")
            if not tid:
                continue

            name = topic.get("name") or ""
            desc = topic.get("description") or ""

            if tid not in topics:
                topics[tid] = {"name": name, "description": desc}

            if tid not in seen_this_title:
                hit_counts[tid] += 1
                if len(examples[tid]) < 3:  # keep catalog compact
                    examples[tid].add(matched or title)
                seen_this_title.add(tid)

        time.sleep(SLEEP_BETWEEN_REQUESTS)

    # Sort by numeric topic id when possible
    def sort_key(tid: str):
        try:
            return (0, int(tid))
        except Exception:
            return (1, str(tid))

    rows = []
    for tid in sorted(topics.keys(), key=sort_key):
        info = topics[tid]
        rows.append((
            tid,
            info.get("name", ""),
            info.get("description", ""),
            hit_counts.get(tid, 0),
            ", ".join(sorted(examples.get(tid, set())))
        ))

    # Write outputs
    assets_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "assets"))
    os.makedirs(assets_dir, exist_ok=True)

    # CSV
    csv_path = os.path.join(assets_dir, "dtdd_topics_catalog.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["topic_id", "topic_name", "description", "hit_count", "example_titles"])
        for tid, name, desc, count, ex in rows:
            w.writerow([tid, name, desc, count, ex])

    # Markdown (compact table + description section)
    md_path = os.path.join(assets_dir, "dtdd_topics_catalog.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# DoesTheDogDie Topics — Catalog (sampled)\n\n")
        f.write(f"Titles sampled: {len(SEED_TITLES)} • Resolved: {resolved} • Skipped: {skipped} • Unique topics: {len(rows)}\n\n")
        f.write("| topic_id | topic_name | hit_count | example_titles |\n")
        f.write("|---|---|---:|---|\n")
        for tid, name, desc, count, ex in rows:
            name_safe = name.replace("|", "\\|")
            ex_safe = ex.replace("|", "\\|")
            f.write(f"| `{tid}` | {name_safe} | {count} | {ex_safe} |\n")

        f.write("\n## Descriptions\n\n")
        for tid, name, desc, count, ex in rows:
            if desc:
                f.write(f"- `{tid}` — {name}: {desc}\n")

    # JSON
    json_path = os.path.join(assets_dir, "dtdd_topics_catalog.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "metadata": {
                    "titles_seeded": len(SEED_TITLES),
                    "processed": processed,
                    "resolved": resolved,
                    "skipped": skipped,
                    "unique_topics": len(rows),
                },
                "topics": [
                    {
                        "topic_id": tid,
                        "topic_name": name,
                        "description": desc,
                        "hit_count": count,
                        "example_titles": ex.split(", ") if ex else [],
                    }
                    for tid, name, desc, count, ex in rows
                ],
            },
            f,
            ensure_ascii=False,
            indent=2,
        )

    # Terminal summary
    print("\nSummary")
    print("-------")
    print(f"Processed titles : {processed}")
    print(f"Resolved items   : {resolved}")
    print(f"Skipped          : {skipped}")
    print(f"Unique topics    : {len(rows)}")
    print("Wrote:")
    print(f"  - {csv_path}")
    print(f"  - {md_path}")
    print(f"  - {json_path}")


if __name__ == "__main__":
    main()