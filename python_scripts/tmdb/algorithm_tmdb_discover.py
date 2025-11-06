"""
algorithm_tmdb_discover.py
--------------------------
Purpose:
    Hit TMDB /discover/movie (filtered search / recommendation)
    and emit a flattened schema table.

Source API:
    https://api.themoviedb.org/3/discover/movie

Output:
    - Writes: python_scripts/assets/schema_tmdb_discover.md
    - Also prints a compact table to the terminal.

Usage (from project root):
    python -m python_scripts.tmdb.algorithm_tmdb_discover

Notes:
    - Requires TMDB_API_KEY in .env
    - Uses DEFAULT_LANGUAGE and DEFAULT_REGION
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md
from python_scripts.shared.constants import DEFAULT_LANGUAGE, DEFAULT_REGION

def main():
    api_key = load_api_key("TMDB_API_KEY")

    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": api_key,
        "language": DEFAULT_LANGUAGE,   # response language
        "region": DEFAULT_REGION,       # scope to US availability context
        "include_adult": "false",
        "sort_by": "popularity.desc",
        "page": 1,
    }

    data = fetch_json(url, params=params)

    title = "TMDB Discover (Movies) Schema"
    source_line = (
        f"Source: TMDB /discover/movie • language={DEFAULT_LANGUAGE}, region={DEFAULT_REGION}, "
        "include_adult=false, sort_by=popularity.desc, page=1."
    )
    outpath = os.path.join(os.path.dirname(__file__), "..", "assets", "schema_tmdb_discover.md")
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