"""
schema_tmdb_external_ids.py
---------------------------

Purpose:
    Fetch external IDs for a movie from TMDB's /movie/{id}/external_ids and
    export a markdown table showing all fields, inferred types, and samples.

Source API:
    https://api.themoviedb.org/3/movie/{id}/external_ids

Output:
    Writes to: python_scripts/assets/schema_tmdb_external_ids.md
    Also prints the table to the terminal.

Usage (from project root):
    python -m python_scripts.tmdb.schema_tmdb_external_ids

Notes:
    - Requires TMDB_API_KEY in your .env (root).
    - Language param included for consistency with other scripts.
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md
from python_scripts.shared.constants import DEFAULT_LANGUAGE

EXAMPLE_MOVIE_ID = 550  # Fight Club

def main():
    api_key = load_api_key("TMDB_API_KEY")

    url = f"https://api.themoviedb.org/3/movie/{EXAMPLE_MOVIE_ID}/external_ids"
    params = {"api_key": api_key, "language": DEFAULT_LANGUAGE}

    data = fetch_json(url, params=params)

    # Write markdown to assets/
    title = "TMDB External IDs Schema"
    source_line = (
        f"Source: TMDB /movie/{{id}}/external_ids with id={EXAMPLE_MOVIE_ID} "
        "(fields below are from this single endpoint response)."
    )
    outpath = os.path.join(os.path.dirname(__file__), "..", "assets", "schema_tmdb_external_ids.md")
    outpath = os.path.normpath(outpath)
    write_md(outpath, title, source_line, data)
    print(f"\n✅ Wrote: {outpath}\n")

    # Also print a compact table to the terminal
    print("Field path".ljust(45), "Type".ljust(12), "Sample value")
    print("-" * 90)
    for path, sample, dtype in flatten(data):
        sample_str = str(sample).replace("\n", " ")[:80]
        print(f"{path.ljust(45)} {dtype.ljust(12)} {sample_str}")

    print(f"\nTotal unique fields: {len(list(flatten(data)))}")

if __name__ == "__main__":
    main()