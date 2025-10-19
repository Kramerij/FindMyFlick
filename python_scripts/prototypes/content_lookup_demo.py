"""
content_lookup_demo.py
----------------

This script takes a movie title as input and retrieves content warnings from 
DoesTheDogDie and general movie info from The Movie Database (TMDB).

It uses environment variables to securely store API keys. 
Results are printed in a simple format.

Requires: 
- TMDB API key (https://www.themoviedb.org/settings/api)
- DoesTheDogDie API key (https://www.doesthedogdie.com/profile)

"""

import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access API keys
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
DTDD_API_KEY = os.getenv('DTDD_API_KEY')

# Get movie title from user
movie_title = input("Enter the movie title: ")

# Search The Movie Database (TMDB) for the movie
tmdb_search_url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}'
tmdb_response = requests.get(tmdb_search_url)
tmdb_data = tmdb_response.json()

if not tmdb_data['results']:
    print(f"No results found for '{movie_title}' on TMDB.")
    exit()

# Ged TMDB ID
tmdb_id = tmdb_data['results'][0]['id']
print(f"TMDB ID for '{movie_title}': {tmdb_id}")

# Get IMDB ID using TMDB
details_url = f'https://api.themoviedb.org/3/movie/{tmdb_id}'
details_params = {'api_key': TMDB_API_KEY, 'append_to_response': 'external_ids'}
details_response = requests.get(details_url, params=details_params)
details_data = details_response.json()  
imdb_id = details_data['external_ids']['imdb_id']
print(f"IMDB ID for '{movie_title}': {imdb_id}")

# Search DoesTheDogDie for the movie using its title
print("\nSearching DoesTheDogDie...")
dtdd_url = f'https://api.doesthedogdie.com/dddsearch'
dtdd_headers = {'Accept': 'application/json', 'x-api-key': DTDD_API_KEY}
dtdd_params = {'q': movie_title}

dtdd_search_response = requests.get(dtdd_url, headers=dtdd_headers, params=dtdd_params)
dtdd_search_data = dtdd_search_response.json()

if not dtdd_search_data['items']:
    print(f"No results found for '{movie_title}' on DoesTheDogDie.")
    exit()

dtdd_id = dtdd_search_data['items'][0]['id']
print(f"DoesTheDogDie ID for '{movie_title}': {dtdd_id}")

# Get trigger warnings from DoesTheDogDie
dtdd_item_url = f'https://api.doesthedogdie.com/media/{dtdd_id}'
dtdd_item_response = requests.get(dtdd_item_url, headers=dtdd_headers)
dtdd_item_data = dtdd_item_response.json()

topic_stats = dtdd_item_data.get('topicItemStats', [])
if not topic_stats:
    print("⚠️ No content warnings found.")
    exit()

# Sort by yesSum descending, but avoid breaking on None
sorted_topics = sorted(
    topic_stats,
    key=lambda t: t.get('yesSum', 0) if t else 0,
    reverse=True
)

print("\n🎬 Content Warnings with Yes Votes:")
found_warning = False

for topic in sorted_topics:
    if topic is None:
        continue

    yes_sum = topic.get('yesSum', 0)
    no_sum = topic.get('noSum', 0)

    if yes_sum > 0:
        topic_info = topic.get('topic') or {}
        name = topic_info.get('name', '[Unnamed Topic]')
        description = (topic_info.get('description') or '').strip()

        # Get sample comment (if any)
        comments = topic.get('comments') or []
        sample_comment = ''
        if comments and isinstance(comments, list) and 'comment' in comments[0]:
            sample_comment = comments[0]['comment'].strip()

        print(f"\n⚠️ {name}")
        print(f"   ✅ Yes votes: {yes_sum}, ❌ No votes: {no_sum}")
        if description:
            print(f"   📌 {description}")
        if sample_comment:
            print(f"   💬 Example: \"{sample_comment}\"")

        found_warning = True

if not found_warning:
    print("⚠️ No confirmed warnings with Yes votes.")