"""
algorithm_tmdb_trending_week.py
-------------------------------
Purpose:
    Hit TMDB /trending/movie/week (current popularity) and emit a schema table.

Source API:
    https://api.themoviedb.org/3/trending/movie/week

Output:
    - Writes: python_scripts/assets/schema_tmdb_trending_week.md
    - Also prints a compact table to the terminal.

Usage (from project root):
    python -m python_scripts.tmdb.algorithm_tmdb_trending_week

Notes:
    - Requires TMDB_API_KEY in .env
    - Uses DEFAULT_LANGUAGE for response localization
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md
from python_scripts.shared.constants import DEFAULT_LANGUAGE

def main():
    api_key = load_api_key("TMDB_API_KEY")

    url = "https://api.themoviedb.org/3/trending/movie/week"
    params = {
        "api_key": api_key,
        "language": DEFAULT_LANGUAGE,
    }

    data = fetch_json(url, params=params)

    title = "TMDB Trending (Movies, Week) Schema"
    source_line = (
        f"Source: TMDB /trending/movie/week • language={DEFAULT_LANGUAGE}."
    )
    outpath = os.path.join(os.path.dirname(__file__), "..", "assets", "schema_tmdb_trending_week.md")
    outpath = os.path.normpath(outpath)
    write_md(outpath, title, source_line, data)
    print(f"\n✅ Wrote: {outpath}\n")

    print("Field path".ljust(55), "Type".ljust(12), "Sample value")
    print("-" * 110)
    for path, sample, dtype in flatten(data):
        sample = str(sample).replace("\n", " ")[:90]
        print(f"{path.ljust(55)} {dtype.ljust(12)} {sample}")

    print(f"\nTotal unique fields: {len(list(flatten(data)))}")

if __name__ == "__main__":
    main()