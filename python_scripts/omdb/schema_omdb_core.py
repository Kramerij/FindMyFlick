"""
schema_omdb_core.py
-------------------
Purpose:
    Fetch a movie from OMDb and export a Markdown table of field paths, inferred types,
    and sample values. Also prints a compact version to the terminal.

Source API:
    http://www.omdbapi.com/?t=<title>&y=<year>&plot=full&r=json&apikey=...

Output:
    Writes: python_scripts/assets/schema_omdb_core_fight_club.md
    Prints: field paths in terminal for quick inspection.

Usage (from project root):
    python -m python_scripts.omdb.schema_omdb_core

Notes:
    - Requires OMDB_API_KEY in .env (root)
    - Uses shared/schema_utils.py for fetching/flattening/markdown
    - Free-tier OMDb keys return "Poster": "N/A" (poster URL is paid feature)
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md

TITLE = "Fight Club"
YEAR = "1999"  # optional; keeps results stable for schema inspection


def main():
    api_key = load_api_key("OMDB_API_KEY")

    url = "http://www.omdbapi.com/"
    params = {
        "t": TITLE,
        "y": YEAR,
        "plot": "full",
        "r": "json",
        "apikey": api_key,
    }

    data = fetch_json(url, params=params)

    print(f"\n=== OMDb: {data.get('Title')} ({data.get('Year')}) ===")
    print(f"Rated: {data.get('Rated')}")
    print(f"Genre: {data.get('Genre')}")
    print(f"Director: {data.get('Director')}")
    print(f"Writer: {data.get('Writer')}")
    print(f"Actors: {data.get('Actors')}")
    print(f"Plot (truncated): {data.get('Plot', '')[:200]}...")
    poster_value = data.get("Poster", "N/A")
    if poster_value == "N/A":
        print("(Poster URL not included — OMDb free-tier key limitation)\n")
    else:
        print(f"Poster: {poster_value}\n")

    # Write schema table (Markdown)
    title = "OMDb Movie Schema (core fields)"
    source_line = f"Source: OMDb by title ('{TITLE}', year '{YEAR or ''}')"
    outpath = os.path.join(
        os.path.dirname(__file__), "..", "assets", "schema_omdb_core_fight_club.md"
    )
    outpath = os.path.normpath(outpath)
    write_md(outpath, title, source_line, data)
    print(f"✅ Wrote: {outpath}\n")

    # Also print a compact table to terminal
    print("Field path".ljust(45), "Type".ljust(12), "Sample value")
    print("-" * 90)
    count = 0
    for path, sample, dtype in flatten(data):
        sample = str(sample).replace("\n", " ")[:80]
        print(f"{path.ljust(45)} {dtype.ljust(12)} {sample}")
        count += 1
    print(f"\nTotal unique fields: {count}")


if __name__ == "__main__":
    main()