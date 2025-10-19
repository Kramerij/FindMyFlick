"""
schema_movie_core.py
--------------------
Purpose:
    Fetch detailed movie information from TMDB's /movie/{id} endpoint and export a
    Markdown table listing every field path, inferred data type, and a short sample value.

Source API:
    https://api.themoviedb.org/3/movie/{id}

Output:
    Writes to: assets/schema_tmdb_movie_core.md
    Also prints the table to the terminal for quick inspection.

Usage:
    Run from the project root:
        python python_scripts/tmdb/schema_movie_core.py

Notes:
    - Requires TMDB_API_KEY in your .env (root of the repo).
    - Uses shared helpers from python_scripts/shared/schema_utils.py.
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md

EXAMPLE_MOVIE_ID = 550  # Fight Club


def main():
    api_key = load_api_key("TMDB_API_KEY")

    url = f"https://api.themoviedb.org/3/movie/{EXAMPLE_MOVIE_ID}"
    params = {"api_key": api_key, "language": "en-US"}

    data = fetch_json(url, params=params)

    title = "TMDB Movie Core Schema"
    source_line = (
        f"Source: TMDB /movie/{{id}} with id={EXAMPLE_MOVIE_ID} "
        "(fields listed below are from this single endpoint response)"
    )

    # --- Write Markdown file ---
    outpath = os.path.join(
        os.path.dirname(__file__), "..", "assets", "schema_tmdb_movie_core.md"
    )
    outpath = os.path.normpath(outpath)
    write_md(outpath, title, source_line, data)
    print(f"\n✅ Wrote: {outpath}\n")

    # --- Also print the results to terminal ---
    print("Field path".ljust(45), "Type".ljust(12), "Sample value")
    print("-" * 90)
    for path, sample, dtype in flatten(data):
        sample = str(sample).replace("\n", " ")[:80]
        print(f"{path.ljust(45)} {dtype.ljust(12)} {sample}")

    print(f"\nTotal unique fields: {len(list(flatten(data)))}")


if __name__ == "__main__":
    main()