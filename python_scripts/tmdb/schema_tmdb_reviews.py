"""
schema_tmdb_reviews.py
----------------------
Purpose:
    Fetch user reviews for a movie from TMDB's /movie/{id}/reviews endpoint and
    export a markdown table of field paths, inferred types, and sample values.
    Also prints a compact table to the terminal.

Source API:
    https://api.themoviedb.org/3/movie/{id}/reviews

Output:
    Writes to: python_scripts/assets/schema_tmdb_reviews.md
    Also prints the table to the terminal.

Usage (run from project root):
    python -m python_scripts.tmdb.schema_tmdb_reviews

Notes:
    - Requires TMDB_API_KEY in your .env
    - Uses shared helpers from python_scripts/shared/schema_utils.py
    - Language set via DEFAULT_LANGUAGE for consistent text fields
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md
from python_scripts.shared.constants import DEFAULT_LANGUAGE

EXAMPLE_MOVIE_ID = 550  # Fight Club

def main():
    api_key = load_api_key("TMDB_API_KEY")

    url = f"https://api.themoviedb.org/3/movie/{EXAMPLE_MOVIE_ID}/reviews"
    params = {
        "api_key": api_key,
        "language": DEFAULT_LANGUAGE,
        "page": 1
    }

    data = fetch_json(url, params=params)

    title = "TMDB Reviews Schema"
    source_line = (
        f"Source: TMDB /movie/{{id}}/reviews with id={EXAMPLE_MOVIE_ID}, "
        f"language={DEFAULT_LANGUAGE}."
    )

    outpath = os.path.join(
        os.path.dirname(__file__), "..", "assets", "schema_tmdb_reviews.md"
    )
    outpath = os.path.normpath(outpath)

    write_md(outpath, title, source_line, data)
    print(f"\n✅ Wrote: {outpath}\n")

    print("Field path".ljust(50), "Type".ljust(12), "Sample value")
    print("-" * 100)
    for path, sample, dtype in flatten(data):
        sample = str(sample).replace("\n", " ")[:90]
        print(f"{path.ljust(50)} {dtype.ljust(12)} {sample}")

    print(f"\nTotal unique fields: {len(list(flatten(data)))}")

if __name__ == "__main__":
    main()