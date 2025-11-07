# FindMyFlick - Python Proof of Concept

## Overview

This folder contains Python proof-of-concept scripts developed as part of the **Find My Flick** Senior Capstone Project.  
The scripts demonstrate how to access and structure data from multiple APIs, including:

- **The Movie Database (TMDB)** – for movie details such as title, release year, genre, cast, directors, writers, and poster images.  
- **DoesTheDogDie (DTDD)** – for content warnings and user-generated sensitivity data.

Some scripts are designed for demonstration (user-facing output), while others focus on identifying API structures and field definitions for later integration into the web application.

---

## Folder Structure

Each schema_*.py script maps a single API endpoint to document available fields, types, and sample values

```
python_scripts/
├── assets/                            # Example outputs (markdown exports and samples)
│   ├── movie_lookup_example.png       # Example Power BI / app output
│   ├── schema_omdb_core_fight_club.md # OMDb sample output for Fight Club
│   ├── schema_tmdb_credits.md         # TMDB /movie/{id}/credits field list
│   ├── schema_tmdb_movie_core.md      # TMDB /movie/{id} field list
│   ├── schema_tmdb_providers.md       # TMDB /movie/{id}/providers (US-only, flatrate or free with ads)
│   ├── schema_tmdb_release_dates.md   # TMDB /movie/{id}/release_dates field list
│   ├── schema_tmdb_images.md          # TMDB /movie/{id}/images field list (posters, backdrops)
│   ├── schema_tmdb_keywords.md        # TMDB /movie/{id}/keywords field list
│   ├── schema_tmdb_external_ids.md    # TMDB /movie/{id}/external_ids field list (for cross-API linking)
│   ├── schema_tmdb_recommendations.md # TMDB /movie/{id}/recommendations (user-similarity algorithm)
│   ├── schema_tmdb_similar.md         # TMDB /movie/{id}/similar (metadata-similarity algorithm)
│   ├── schema_tmdb_discover.md        # TMDB /discover/movie (filtered search / recommendation algorithm)
│   └── schema_tmdb_trending_week.md   # TMDB /trending/movie/week (current popularity algorithm)
│
├── dtdd/                              # Scripts for analyzing DoesTheDogDie API endpoints
│   └── schema_dtdd_topics_catalog.py  # Aggregates unique topics across many sampled movies
│
├── omdb/                              # Scripts for analyzing OMDb API endpoint
│   └── schema_omdb_core.py            # Core movie metadata including MPAA rating, year, and language
│
├── tmdb/                              # Scripts for analyzing TMDB API endpoints
│   ├── schema_tmdb_credits.py         # Actors, directors, and crew members
│   ├── schema_tmdb_movie_core.py      # General movie info (poster path, release date, genre, etc.)
│   ├── schema_tmdb_providers.py       # Paid subscription and ad-supported streaming providers (US-only)
│   ├── schema_tmdb_release_dates.py   # Full release date info including region and certification
│   ├── schema_tmdb_images.py          # Image metadata (posters, backdrops)
│   ├── schema_tmdb_keywords.py        # Movie keywords and tags
│   ├── schema_tmdb_external_ids.py    # External identifiers (IMDb, Facebook, Instagram, Twitter)
│   │
│   ├── algorithm_tmdb_recommendations.py # User-similarity recommendation engine
│   ├── algorithm_tmdb_similar.py         # Metadata-similarity recommendation engine
│   ├── algorithm_tmdb_discover.py        # Filtered search / hybrid recommendation system
│   └── algorithm_tmdb_trending_week.py   # Current popularity algorithm
│
├── shared/                            # Shared helpers for fetching, flattening, and scoping API data
│   ├── constants.py                   # Language and region defaults (US market, English text)
│   └── schema_utils.py                # Flatten JSON and export markdown tables
│
├── content_warnings/                  # DoesTheDogDie taxonomy and processing scripts
│   ├── data/
│   │   └── dtdd/
│   │       └── dtdd_topics_catalog.json     # Raw DoesTheDogDie topics export (200+ entries)
│   │
│   └── taxonomy/
│       ├── umbrellas.json                  # Tier-1 umbrella categories (12 total)
│       ├── claude_taxonomy.yml             # Tier-2 subcategories mapped to DTDD topic IDs
│       ├── structure_report.md             # Human-readable summary + validation
│       ├── expanded.json                   # Backend-ready taxonomy for integration
│       ├── build_structure_report.py       # Generates structure_report.md
│       └── build_expanded_json.py          # Generates expanded.json
│
└── README.md                          # This file
```

---

## Setup

1. **Install Python (if not already installed):**
   - [Download Python](https://www.python.org/downloads/) (version 3.9 or later recommended).
   - Make sure to check the option to "Add Python to PATH" during installation.

2. **Copy the environment template:**
   Run the following command in your terminal:
   ```
   cp python_scripts/.env.template python_scripts/.env
   ```
   
   Then edit .env and fill in your API keys:
   - [TMDB API key](https://www.themoviedb.org/settings/api)
   - [DoesTheDogDie API key](https://www.doesthedogdie.com/profile)
   - [OMDb API key](http://www.omdbapi.com/apikey.aspx)

3. **(Optional but recommended) Create and activate a virtual environment:**
   Run the following command in your terminal:
   ```
   python -m venv .venv
   .\.venv\Scripts\activate   # On Windows
   source .venv/bin/activate     # On macOS/Linux
   ```
   
4. **Install required packages:**
   Run the following command in your terminal:
   ```
   pip install -r requirements.txt
   ```
   
5. **Run the script:**
   Make sure your virtual environment is active and your `.env` has `TMDB_API_KEY` (and any other keys needed).
   Run the following commands in your terminal:

### Demo script (content warnings):
```
python python_scripts/prototypes/movie_lookup_demo.py
```


### Schema / API-mapping scripts (TMDB example):
Run **from the project root** using module syntax so imports from `python_scripts.shared` resolve:
```
python -m python_scripts.tmdb.schema_movie_core
```


The script uses a built-in `EXAMPLE_MOVIE_ID`.  
If you want to try a different movie ID temporarily, you can:

- **Option A (edit constant):** open `python_scripts/tmdb/schema_movie_core.py` and change `EXAMPLE_MOVIE_ID`.
- **Option B (env var override)**

macOS/Linux:
```
TMDB_MOVIE_ID=603 python -m python_scripts.tmdb.schema_movie_core
```

Windows PowerShell (session only):
```
$env:TMDB_MOVIE_ID = "603"
python -m python_scripts.tmdb.schema_movie_core
```


### Where the results go:

- You’ll see a formatted table in the terminal.
- A Markdown export is also written here:
  ```
  python_scripts/assets/schema_tmdb_movie_core.md
  ```

---

## Content Warning Taxonomy (DoesTheDogDie)

This folder defines how DoesTheDogDie (DTDD) topics are grouped into broader categories for FindMyFlick.  
It converts over 200 individual content warnings into 12 Tier-1 *umbrella* categories with nested Tier-2 subcategories.

### Purpose
- Simplifies search and filtering for sensitive content.
- Lets users filter at either a high-level (e.g., “Animal Harm & Death”) or specific topic level.
- Provides a static JSON (`expanded.json`) that maps each DTDD topic ID to its umbrella category.

### How It Works
1. **`dtdd_topics_catalog.json`** — the raw topic list pulled from the DoesTheDogDie API.  
2. **`umbrellas.json`** — defines the 12 high-level umbrella categories.  
3. **`claude_taxonomy.yml`** — groups topic IDs under each umbrella and subcategory.  
4. **`build_structure_report.py`** — generates a readable Markdown report (`structure_report.md`) summarizing Tier-1 and Tier-2 layout.  
5. **`build_expanded_json.py`** — builds `expanded.json`, the file actually used by the backend.

### Developer Notes
If you update the taxonomy and need to rebuild outputs:
```bash
pip install pyyaml
python python_scripts/content_warnings/taxonomy/build_structure_report.py
python python_scripts/content_warnings/taxonomy/build_expanded_json.py
```

The second script writes `expanded.json`, which the backend can load like this:

```python
import json
from pathlib import Path

taxonomy = json.loads(
    Path("python_scripts/content_warnings/taxonomy/expanded.json").read_text(encoding="utf-8")
)
```

# Example lookups:
animal_ids = taxonomy["umbrella_to_topic_ids"]["U01"]
topic_name = taxonomy["topics"]["153"]["topic_name"]
umbrellas_for_topic = taxonomy["topic_id_to_umbrellas"]["153"]
This file is static and can be imported directly into backend code or used for front-end filtering logic.
---

## Example Output

- Screenshot of the demo script:
  ![Example Output](python_scripts/assets/movie_lookup_example.png)

- Markdown export of TMDB `/movie/{id}` fields:
  [schema_tmdb_movie_core.md](python_scripts/assets/schema_tmdb_movie_core.md)



## References

- Portions of the Python scripts were written and debugged with assistance from IntelliSense and integrated AI development tools in Visual Studio Code.
