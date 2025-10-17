import os, requests, json
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

movie_id = 550  # Fight Club
url = f"https://api.themoviedb.org/3/movie/{movie_id}"
params = {"api_key": TMDB_API_KEY}  # <-- no append_to_response here
resp = requests.get(url, params=params)
resp.raise_for_status()
data = resp.json()

# Show just the top-level keys, type, and a short example
print("Top-level fields from /movie/{id}:\n")
for k, v in data.items():
    t = type(v).__name__
    sample = v
    # keep example short
    if isinstance(sample, str) and len(sample) > 120:
        sample = sample[:120] + "…"
    print(f"- {k:20} • {t:8} • {sample}")
