"""
schema_tmdb_images.py
---------------------
Purpose:
    Fetch posters/backdrops from TMDB's /movie/{id}/images endpoint and export a
    Markdown table listing each field path, inferred type, and a short sample.
    Also prints the schema to the terminal.

Source API:
    https://api.themoviedb.org/3/movie/{id}/images

Output:
    Writes to: python_scripts/assets/schema_tmdb_images.md
    Prints a compact table to the terminal.

Usage (from project root):
    python -m python_scripts.tmdb.schema_tmdb_images

Notes:
    - Requires TMDB_API_KEY in your .env (root of repo).
    - Images support `language` and `include_image_language`.
      We request English plus language-agnostic: include_image_language=en,null
    - Uses shared helpers from python_scripts/shared/schema_utils.py.
"""

import os
from python_scripts.shared.schema_utils import load_api_key, fetch_json, flatten, write_md
from python_scripts.shared.constants import DEFAULT_LANGUAGE

EXAMPLE_MOVIE_ID = 550  # Fight Club

def main():
    api_key = load_api_key("TMDB_API_KEY")

    url = f"https://api.themoviedb.org/3/movie/{EXAMPLE_MOVIE_ID}/images"
    params = {
        "api_key": api_key,
        "language": DEFAULT_LANGUAGE,            # labels where applicable
        "include_image_language": "en,null",     # english + language-agnostic
    }

    data = fetch_json(url, params=params)

    title = "TMDB Movie Images Schema"
    source_line = (
        f"Source: TMDB /movie/{{id}}/images with id={EXAMPLE_MOVIE_ID}, "
        f"language={DEFAULT_LANGUAGE}, include_image_language=en,null"
    )

    outpath = os.path.join(
        os.path.dirname(__file__), "..", "assets", "schema_tmdb_images.md"
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