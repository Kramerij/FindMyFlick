"""
schema_dtdd_search.py
---------------------
Purpose:
    Show the schema of DoesTheDogDie search results (/dddsearch?q=...).

Output:
    - python_scripts/assets/dtdd_search_fight_club.md
    - Also prints a flattened field/type/sample table to the terminal.

Usage:
    From project root:
        python -m python_scripts.dtdd.schema_dtdd_search

Notes:
    - Requires DTDD_API_KEY in your .env (root).
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md

EXAMPLE_TITLE = "Fight Club"  # change if you want another seed

def main():
    api_key = load_api_key("DTDD_API_KEY")

    url = "https://api.doesthedogdie.com/dddsearch"
    headers = {"Accept": "application/json", "x-api-key": api_key}
    params = {"q": EXAMPLE_TITLE}

    data = fetch_json(url, params=params, headers=headers)

    # Write markdown
    assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    assets_dir = os.path.normpath(assets_dir)
    os.makedirs(assets_dir, exist_ok=True)

    title = "DTDD Search Schema"
    source_line = f"Source: /dddsearch?q={EXAMPLE_TITLE!r}"
    outpath = os.path.join(assets_dir, "dtdd_search_fight_club.md")
    write_md(outpath, title, source_line, data)

    print(f"\n✅ Wrote: {outpath}\n")

    # Terminal table
    print("Field path".ljust(60), "Type".ljust(10), "Sample value")
    print("-" * 100)
    for path, sample, dtype in flatten(data):
        sample = str(sample).replace("\n", " ")[:90]
        print(f"{path.ljust(60)} {dtype.ljust(10)} {sample}")

    print(f"\nTotal unique fields: {len(list(flatten(data)))}")

if __name__ == "__main__":
    main()