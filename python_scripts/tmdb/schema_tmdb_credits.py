"""
schema_tmdb_credits.py
----------------------
Fetch cast & crew from TMDB's `/movie/{id}/credits` endpoint and export a
Markdown table listing every field path, inferred data type, and a short sample value.

Source API:
  https://developer.themoviedb.org/reference/movie-credits

Outputs:
  Writes to: python_scripts/assets/schema_tmdb_credits.md
  Also prints the table to the terminal for quick inspection.

Usage (from project root):
  python -m python_scripts.tmdb.schema_tmdb_credits

Notes:
  - Requires TMDB_API_KEY in your .env (root of repo).
  - Uses shared helpers from python_scripts/shared/schema_utils.py.
"""

from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md

EXAMPLE_MOVIE_ID = 550  # Fight Club

def main():
    api_key = load_api_key("TMDB_API_KEY")

    url = f"https://api.themoviedb.org/3/movie/{EXAMPLE_MOVIE_ID}/credits"
    params = {"api_key": api_key, "language": "en-US"}
    data = fetch_json(url, params=params)

    # --- Terminal preview ---
    rows = list(flatten(data))
    print("Field path".ljust(45), "Type".ljust(12), "Sample value")
    print("-" * 90)
    for p, sample, t in rows:
        print(p.ljust(45), t.ljust(12), sample)
    print(f"\nTotal unique fields: {len(rows)}\n")

    # --- Markdown export ---
    title = "TMDB: /movie/{id}/credits schema (Fight Club, id=550)"
    source_line = f"Source: https://api.themoviedb.org/3/movie/{EXAMPLE_MOVIE_ID}/credits"
    outpath = "python_scripts/assets/schema_tmdb_credits.md"
    write_md(outpath, title, source_line, data)
    print(f"✅ Wrote: {outpath}")

if __name__ == "__main__":
    main()