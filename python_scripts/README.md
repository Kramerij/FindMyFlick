# FindMyFlick - Python Proof of Concept

## Overview

This script allows users to look up a movie and get:
- Content warnings from DoesTheDogDie (e.g., violence, animal harm, etc.)
- General movie information from The Movie Database (TMDB)

API keys are required from both services and stored securely in a `.env` file.

---

## Setup

1. **Install Python (if not already installed):**
   - [Download Python](https://www.python.org/downloads/) (version 3.9 or later recommended).
   - Make sure to check the option to "Add Python to PATH" during installation.

2. **Copy the environment template:**
   Run the following command in your terminal:
   cp python_scripts/.env.template python_scripts/.env
   
   Then fill in your API keys:
   - [TMDB API key](https://www.themoviedb.org/settings/api)
   - [DoesTheDogDie API key](https://www.doesthedogdie.com/profile)

3. **(Optional but recommended) Create and activate a virtual environment:**
   Run the following command in your terminal:
   python -m venv .venv
   .\.venv\Scripts\activate   # On Windows
   source .venv/bin/activate     # On macOS/Linux
   

4. **Install required packages:**
   Run the following command in your terminal:
   pip install -r requirements.txt
   

5. **Run the script:**
   Run the following command in your terminal:
   python python_scripts/movie_lookup.py
   

---

## Example Output

Here is a snippet of what the script output looks like:

![Example Output](python_scripts/assets/movie_lookup_example.png)

---

## References

- Portions of the movie_lookup.py script were written and debugged with assistance from IntelliSense and AI coding tools in VS Code.
