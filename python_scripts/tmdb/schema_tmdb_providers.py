"""
schema_tmdb_providers.py
------------------------
Purpose:
    Fetch "Where to Watch" data for a movie from TMDB's /movie/{id}/watch/providers,
    then (a) print only US subscription ("flatrate") and free-with-ads ("ads") providers,
    and (b) export a markdown table of the filtered US block to assets.

Source API:
    https://api.themoviedb.org/3/movie/{id}/watch/providers

Output:
    Writes to: python_scripts/assets/schema_tmdb_providers.md
    Also prints friendly provider lists + the filtered US schema table to the terminal.

Usage (from project root):
    python -m python_scripts.tmdb.schema_tmdb_providers

Notes:
    - Requires TMDB_API_KEY in your .env (root of the repo).
    - Uses shared helpers from python_scripts/shared/schema_utils.py.
    - Region is limited to US via DEFAULT_REGION from shared/constants.
"""

import os
from python_scripts.shared.schema_utils import (
    load_api_key,
    fetch_json,
    flatten,
    write_md,
)
from python_scripts.shared.constants import DEFAULT_REGION

# Example movie: Fight Club
EXAMPLE_MOVIE_ID = 550  # change if you want to test another title


def names(items):
    """Return sorted unique provider names from a list of provider dicts."""
    return sorted({p.get("provider_name", "?") for p in (items or [])})


def main():
    api_key = load_api_key("TMDB_API_KEY")

    url = f"https://api.themoviedb.org/3/movie/{EXAMPLE_MOVIE_ID}/watch/providers"
    # Endpoint doesn't need language; we filter the region client-side.
    params = {"api_key": api_key}

    data = fetch_json(url, params=params) or {}
    us_block = (data.get("results") or {}).get(DEFAULT_REGION, {})

    if not us_block:
        print(f"\nNo provider data found for region {DEFAULT_REGION}.")
        # still write an empty markdown with context so readers know what was attempted
        title = "TMDB Watch Providers (US) — Filtered Schema"
        source_line = (
            f"Source: TMDB /movie/{{id}}/watch/providers with id={EXAMPLE_MOVIE_ID}, "
            f"region={DEFAULT_REGION}. Only `flatrate` (subscription) and `ads` (free with ads) "
            f"providers are included; `rent` and `buy` are excluded."
        )
        outpath = os.path.join(
            os.path.dirname(__file__), "..", "assets", "schema_tmdb_providers.md"
        )
        outpath = os.path.normpath(outpath)
        write_md(outpath, title, source_line, {})
        print(f"\n✅ Wrote: {outpath}\n")
        return

    # Friendly lists (only what you asked for)
    subs = us_block.get("flatrate", [])   # subscription services
    free_ads = us_block.get("ads", [])    # free with ads

    # OPTIONAL: limit to a curated set of major subscription services.
    # Uncomment and adjust if your team decides to whitelist providers.
    #
    # MAJOR_SUBS = {
    #     "Netflix", "Hulu", "Max", "Prime Video", "Peacock", "Paramount+",
    #     "Disney+", "Apple TV+"
    # }
    # subs = [p for p in subs if p.get("provider_name") in MAJOR_SUBS]

    # ---------- Print friendly lists ----------
    print("\nUS Subscription (flatrate):")
    print("  " + (", ".join(names(subs)) or "None"))

    print("\nUS Free with ads (ads):")
    print("  " + (", ".join(names(free_ads)) or "None"))

    # ---------- Keep only selected categories for schema/markdown ----------
    filtered_us = {
        "link": us_block.get("link"),
        "flatrate": subs or [],
        "ads": free_ads or [],
    }

    # ---------- Print a schema table (filtered US block only) ----------
    print("\nField path".ljust(50), "Type".ljust(12), "Sample value")
    print("-" * 100)
    for path, sample, dtype in flatten(filtered_us):
        sample = str(sample).replace("\n", " ")[:90]
        print(f"{path.ljust(50)} {dtype.ljust(12)} {sample}")

    # Count unique paths for filtered US block
    print(f"\nTotal unique fields: {len(list(flatten(filtered_us)))}")

    # ---------- Write Markdown (filtered US block) ----------
    title = "TMDB Watch Providers (US) — Filtered Schema"
    source_line = (
        f"Source: TMDB /movie/{{id}}/watch/providers with id={EXAMPLE_MOVIE_ID}, "
        f"region={DEFAULT_REGION}. Only `flatrate` (subscription) and `ads` (free with ads) "
        f"providers are included; `rent` and `buy` are excluded."
    )
    outpath = os.path.join(
        os.path.dirname(__file__), "..", "assets", "schema_tmdb_providers.md"
    )
    outpath = os.path.normpath(outpath)
    write_md(outpath, title, source_line, filtered_us)

    print(f"\n✅ Wrote: {outpath}\n")


if __name__ == "__main__":
    main()