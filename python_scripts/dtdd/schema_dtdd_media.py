"""
schema_dtdd_media.py
--------------------
Purpose:
    Resolve a DoesTheDogDie itemId by title search, then fetch and
    show the schema of /media/{itemId} (topics, comments, etc.).

Output:
    - python_scripts/assets/dtdd_media_fight_club.md
    - Also prints a flattened field/type/sample table to the terminal.

Usage:
    From project root:
        python -m python_scripts.dtdd.schema_dtdd_media

Notes:
    - Requires DTDD_API_KEY in your .env (root).
    - Uses title search only to avoid IMDb lookup brittleness.
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md

EXAMPLE_TITLE = "Fight Club"  # change if desired

def dtdd_find_item_by_title(api_key: str, title: str):
    url = "https://api.doesthedogdie.com/dddsearch"
    headers = {"Accept": "application/json", "x-api-key": api_key}
    params = {"q": title}
    data = fetch_json(url, params=params, headers=headers)
    items = (data or {}).get("items", [])
    return items[0] if items else None

def main():
    api_key = load_api_key("DTDD_API_KEY")

    # 1) Resolve item by title search (kept simple and reliable)
    item = dtdd_find_item_by_title(api_key, EXAMPLE_TITLE)
    if not item:
        raise RuntimeError(f"No DTDD item found for title {EXAMPLE_TITLE!r}")

    item_id = item.get("id")
    if not item_id:
        raise RuntimeError("DTDD search returned an item without 'id'")

    # 2) Fetch media object
    url = f"https://api.doesthedogdie.com/media/{item_id}"
    headers = {"Accept": "application/json", "x-api-key": api_key}
    media = fetch_json(url, headers=headers)

    # Write markdown
    assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    assets_dir = os.path.normpath(assets_dir)
    os.makedirs(assets_dir, exist_ok=True)

    title = "DTDD Media Schema"
    source_line = f"Source: /dddsearch?q={EXAMPLE_TITLE!r} → /media/{item_id}"
    outpath = os.path.join(assets_dir, "dtdd_media_fight_club.md")
    write_md(outpath, title, source_line, media)

    print(f"\n✅ Wrote: {outpath}\n")

    # Terminal table
    print("Field path".ljust(60), "Type".ljust(10), "Sample value")
    print("-" * 100)
    for path, sample, dtype in flatten(media):
        sample = str(sample).replace("\n", " ")[:90]
        print(f"{path.ljust(60)} {dtype.ljust(10)} {sample}")

    print(f"\nTotal unique fields: {len(list(flatten(media)))}")

if __name__ == "__main__":
    main()