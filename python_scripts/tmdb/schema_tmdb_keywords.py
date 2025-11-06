"""
schema_tmdb_keywords.py
-----------------------
Purpose:
    Fetch keyword tags for a movie from TMDB's /movie/{id}/keywords endpoint and
    export a Markdown table listing each field path, inferred type, and a short sample.
    Also prints the schema to the terminal.

Source API:
    https://api.themoviedb.org/3/movie/{id}/keywords

Output:
    Writes to: python_scripts/assets/schema_tmdb_keywords.md
    Prints a compact table to the terminal.

Usage (from project root):
    python -m python_scripts.tmdb.schema_tmdb_keywords

Notes:
    - Requires TMDB_API_KEY in your .env (root of repo).
    - Endpoint ignores language; keywords are language-agnostic.
    - Uses shared helpers from python_scripts/shared/schema_utils.py.
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md

EXAMPLE_MOVIE_ID = 550  # Fight Club

def main():
    api_key = load_api_key("TMDB_API_KEY")

    url = f"https://api.themoviedb.org/3/movie/{EXAMPLE_MOVIE_ID}/keywords"
    params = {"api_key": api_key}  # language not supported here

    data = fetch_json(url, params=params)

    title = "TMDB Movie Keywords Schema"
    source_line = (
        f"Source: TMDB /movie/{{id}}/keywords with id={EXAMPLE_MOVIE_ID} "
        "(keywords are language-agnostic)"
    )

    # Write Markdown next to other assets
    outpath = os.path.join(
        os.path.dirname(__file__), "..", "assets", "schema_tmdb_keywords.md"
    )
    outpath = os.path.normpath(outpath)
    write_md(outpath, title, source_line, data)
    print(f"\n✅ Wrote: {outpath}\n")

    # Print compact table to terminal
    print("Field path".ljust(50), "Type".ljust(12), "Sample value")
    print("-" * 100)
    for path, sample, dtype in flatten(data):
        sample = str(sample).replace("\n", " ")[:90]
        print(f"{path.ljust(50)} {dtype.ljust(12)} {sample}")

    from collections import deque
    count = len(list(flatten(data)))
    print(f"\nTotal unique fields: {count}")

if __name__ == "__main__":
    main()