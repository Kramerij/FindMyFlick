"""
algorithm_tmdb_recommendations.py
---------------------------------
Purpose:
    Fetch TMDB recommendations for a given movie id from /movie/{id}/recommendations
    and emit a flattened schema table (field path, inferred type, sample).

Source API:
    https://api.themoviedb.org/3/movie/{id}/recommendations

Output:
    - Writes: python_scripts/assets/schema_tmdb_recommendations.md
    - Also prints a compact table to the terminal.

Usage (from project root):
    python -m python_scripts.tmdb.algorithm_tmdb_recommendations

Notes:
    - Requires TMDB_API_KEY in .env
    - Uses language from shared/constants (US English text)
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md
from python_scripts.shared.constants import DEFAULT_LANGUAGE

EXAMPLE_MOVIE_ID = 550  # Fight Club


def main():
    api_key = load_api_key("TMDB_API_KEY")

    url = f"https://api.themoviedb.org/3/movie/{EXAMPLE_MOVIE_ID}/recommendations"
    params = {
        "api_key": api_key,
        "language": DEFAULT_LANGUAGE,
        "page": 1,
    }

    data = fetch_json(url, params=params)

    # ---- Write Markdown file ----
    title = "TMDB Recommendations Schema"
    source_line = (
        f"Source: TMDB /movie/{{id}}/recommendations with id={EXAMPLE_MOVIE_ID}, "
        f"language={DEFAULT_LANGUAGE}."
    )
    outpath = os.path.join(
        os.path.dirname(__file__), "..", "assets", "schema_tmdb_recommendations.md"
    )
    outpath = os.path.normpath(outpath)
    write_md(outpath, title, source_line, data)
    print(f"\n✅ Wrote: {outpath}\n")

    # ---- Print compact table to terminal ----
    print("Field path".ljust(55), "Type".ljust(12), "Sample value")
    print("-" * 110)
    for path, sample, dtype in flatten(data):
        sample = str(sample).replace("\n", " ")[:90]
        print(f"{path.ljust(55)} {dtype.ljust(12)} {sample}")

    print(f"\nTotal unique fields: {len(list(flatten(data)))}")


if __name__ == "__main__":
    main()