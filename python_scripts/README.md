# FindMyFlick - Python Proof of Concept

## Overview

This folder contains Python proof-of-concept scripts developed as part of the **Find My Flick** Senior Capstone Project.  
The scripts demonstrate how to access and structure data from multiple APIs, including:

- **The Movie Database (TMDB)** – for movie details such as title, release year, genre, cast, directors, writers, and poster images.  
- **DoesTheDogDie (DTDD)** – for content warnings and user-generated sensitivity data.

Some scripts are designed for demonstration (user-facing output), while others focus on identifying API structures and field definitions for later integration into the web application.

---

## Folder Structure

```
python_scripts/
├── assets/                 # Example outputs (screenshots, markdown exports)
├── prototypes/             # Early demo scripts such as content lookup
├── shared/                 # Shared helpers for fetching and flattening API data
├── tmdb/                   # Scripts for analyzing TMDB API endpoints
│   └── schema_movie_core.py
└── README.md               # This file
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

## Example Output

- Screenshot of the demo script:
  ![Example Output](python_scripts/assets/movie_lookup_example.png)

- Markdown export of TMDB `/movie/{id}` fields:
  [schema_tmdb_movie_core.md](python_scripts/assets/schema_tmdb_movie_core.md)

---

## References

- Portions of the Python scripts were written and debugged with assistance from IntelliSense and integrated AI development tools in Visual Studio Code.
