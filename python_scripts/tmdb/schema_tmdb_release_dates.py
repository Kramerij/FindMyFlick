"""
schema_tmdb_release_dates.py
--------------------
Purpose:
    Fetch region-specific release information from TMDB's /movie/{id}/release_dates endpoint
    and export a Markdown table listing each field path, inferred data type, and a short sample value.

Source API:
    https://api.themoviedb.org/3/movie/{id}/release_dates

Output:
    Writes to: python_scripts/assets/schema_tmdb_release_dates.md
    Also prints the table to the terminal for quick inspection.

Usage:
    From the project root:
        python -m python_scripts.tmdb.schema_tmdb_release_dates

Notes:
    - Requires TMDB_API_KEY in your .env (root of the repo).
    - Uses shared helpers from python_scripts/shared/schema_utils.py.
    - Restricted to US region data.
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md
from python_scripts.shared.constants import DEFAULT_LANGUAGE

EXAMPLE_MOVIE_ID = 550  # Fight Club
REGION = "US"


def main():
    api_key = load_api_key("TMDB_API_KEY")

    url = f"https://api.themoviedb.org/3/movie/{EXAMPLE_MOVIE_ID}/release_dates"
    params = {"api_key": api_key, "language": DEFAULT_LANGUAGE}

    data = fetch_json(url, params=params)

    # Filter to only US releases if present
    results = data.get("results", [])
    us_result = next((r for r in results if r.get("iso_3166_1") == REGION), None)
    if not us_result:
        print(f"⚠️ No release info found for region {REGION}. Showing full dataset.")
        region_data = data
    else:
        region_data = us_result

    title = "TMDB Release Dates (US Region)"
    source_line = (
        f"Source: TMDB /movie/{{id}}/release_dates for id={EXAMPLE_MOVIE_ID} "
        f"(restricted to region={REGION})"
    )

    outpath = os.path.join(
        os.path.dirname(__file__), "..", "assets", "schema_tmdb_release_dates.md"
    )
    outpath = os.path.normpath(outpath)
    write_md(outpath, title, source_line, region_data)
    print(f"\n✅ Wrote: {outpath}\n")

    # Print results to terminal
    rows = list(flatten(region_data))
    print("Field path".ljust(55), "Type".ljust(12), "Sample value")
    print("-" * 100)
    for path, sample, dtype in rows:
        sample = str(sample).replace("\n", " ")[:80]
        print(f"{path.ljust(55)} {dtype.ljust(12)} {sample}")

    print(f"\nTotal unique fields: {len(rows)}")


if __name__ == "__main__":
    main()