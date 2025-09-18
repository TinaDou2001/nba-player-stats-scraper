# NBA Player Stats (Medians) + Ranked Probabilities

A simple Flask web app that:
- Scrapes player **game logs** from Basketball Reference  
- Cleans the data with **pandas** and computes **medians**  
- Lets you choose a stat (PTS/TRB/AST/etc.) and shows a **ranked list** of all game results with:
  - empirical **P(X ≥ value)** (tail probability)  
  - **American moneyline** implied from that probability  
  - the **median** highlighted

> **Note:** This app scrapes public pages via `pandas.read_html` with a standard User-Agent. Please use responsibly.

---

## Demo (How it works)

1. Enter a player (e.g., `LeBron James`).  
2. Pick a season (e.g., `2024` for the 2023–24 season).  
3. Pick a category (`PTS`, `TRB`, `AST`, etc.).  
4. Hit **Get Stats**.  
5. You’ll see:
   - A medians panel for all numeric columns  
   - A ranked list for your chosen stat with **probability** and **implied American odds** (+/−)

---

## Tech Stack

- **Python**: Flask, requests, BeautifulSoup, pandas, lxml  
- **Frontend**: HTML + CSS (Jinja templates)  
- **Scraping**: `pandas.read_html` + small HTML parsing helpers

---

## Project Structure
nba-player-stats-scraper/
├─ app.py # Flask app & routes
├─ nba_scraper.py # scraping + cleaning helpers
├─ requirements.txt # python deps
└─ templates/
└─ index.html # main UI