# Tina Dou

## Description

This project, **NBA Player Performance Dashboard**, aims to give users an interactive way to explore a single NBA player’s game-by-game performance across a season.  

By combining web-scraped data from Basketball Reference with interactive charts, the app will help users visualize how a player’s performance changes over time and how consistently they achieve certain scoring, rebounding, or assisting thresholds.  

Users will be able to:
- Select **a player**, **a season**, and a **stat category** (e.g., Points, Assists, Rebounds).  
- See the player’s **performance trend** across all games in that season.  
- Explore an **interactive histogram** showing the distribution of game outcomes.  
- View a **ranked probability list** with implied betting odds for hitting specific stat lines.  

The goal is to make player performance patterns intuitive and interactive for basketball fans who want to explore data visually rather than read raw stats.

---

## Technical Plan re: Option B

### Option
I am pursuing **Option B (Dynamic Ensemble)** because I will include multiple coordinated visualizations (trend line, histogram, probability list) that update based on user selections.  
This structure allows for meaningful interaction without the complexity of a large-scale simulation.

### Libraries and Tools
- **Flask** (Python backend) — to handle routing and dynamically fetch player data  
- **BeautifulSoup + pandas** — to scrape and clean game logs from Basketball Reference  
- **Altair / Vega-Lite** — to create interactive visualizations embedded in HTML  
- **HTML + CSS + JavaScript (Jinja templates)** — for the dashboard layout and dropdown interactivity  

### Planned Visualizations
1. **Trend Chart:**  
   A line or area chart showing game-by-game points (or other chosen stat) throughout the season.  
   Hovering displays the date, opponent, and game result.

2. **Distribution Chart:**  
   Interactive histogram showing how often the player achieved specific stat values.  
   The user can toggle between PTS, TRB, and AST.

3. **Probability & Odds Table:**  
   A ranked list that displays the empirical probability of the player exceeding each stat level and the corresponding implied American odds.  
   The player’s **median** performance will be highlighted visually.  

### Inspirations
https://us-energy-akshar.netlify.app/
https://storm-is-brewing.netlify.app/

---

## Mockup

![](Sketch.png)

**Sketch Description:**  
- **Top bar:** Dropdowns for Player, Season, and Stat Category.  
- **Top section:** Line chart showing game-by-game performance with a bold line and hover tooltips.  
- **Bottom left section:** Histogram visualizing how often the player achieved specific values.  
- **Bottom right section:** Scrollable table listing each possible stat value, empirical probability, implied odds, and median highlight.

---

## Data Sources

### Data Source 1: Basketball Reference (Game Logs)

**URL:** https://www.basketball-reference.com/  
**Size:** uncountable, because of the number of inactive and active players are all included 
**Description:**  
Each player’s game log includes per-game statistics such as Points (PTS), Rebounds (TRB), Assists (AST), FG%, 3P%, FT%, and more.  
I am already using BeautifulSoup and pandas to scrape and clean this data for selected players.  
Each query retrieves only the relevant season’s data, which I then process to compute medians and probabilities.

---

## Questions

1. Would embedding multiple Altair charts with linked dropdowns meet the “interactive enough” threshold for Option B, or should I incorporate one D3.js chart?

---
