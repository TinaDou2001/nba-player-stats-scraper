import requests
from bs4 import BeautifulSoup
import pandas as pd
import statistics

# Step 1: Get player's Basketball Reference suffix
def get_player_suffix(player_name):
    # LeBron James will give you j
    last_name_letter = player_name.split()[-1][0].lower()
    index_url = f"https://www.basketball-reference.com/players/{last_name_letter}/"
    # this will be https://www.basketball-reference.com/players/j/
    headers = {"User-Agent": "Mozilla/5.0"}
    # sends an HTTP GET request to the index_url
    # stores the response (HTML page) in the variable res
    res = requests.get(index_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    for row in soup.select("table tbody tr"):
        name_cell = row.find("th", {"data-stat": "player"})
        if name_cell and player_name.lower() in name_cell.text.lower():
            suffix = name_cell["data-append-csv"]
            return suffix
    return None

# Step 2