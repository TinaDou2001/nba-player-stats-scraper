from datetime import datetime
from flask import Flask, request, render_template
from nba_scraper import get_player_suffix, get_game_log_table, calculate_medians
import pandas as pd

app = Flask(__name__)

def prob_to_american(p: float) -> str:
    """Return American odds from implied probability p (0<p<1)."""
    if p <= 0 or p >= 1:
        return "—"
    if p <= 0.5:
        ml = round(100 * (1 - p) / p)
        return f"+{ml}"
    else:
        ml = round(-100 * p / (1 - p))
        return f"{ml}"

@app.route("/", methods=["GET", "POST"])
def index():
    medians = None
    player_name = ""
    selected_season = "2024"
    selected_category = "PTS"  # default
    current_year = datetime.now().year
    years = list(range(current_year, 2003, -1))

    ranked_items = None

    if request.method == "POST":
        player_name = request.form.get("player_name", "").strip()
        selected_season = request.form.get("season", "2024")
        selected_category = request.form.get("category", "PTS")

        if player_name:
            suffix = get_player_suffix(player_name)
            if suffix:
                df = get_game_log_table(suffix, selected_season)
                if df is not None and selected_category in df.columns:
                    # medians for highlight
                    medians = calculate_medians(df)
                    median_val = None
                    if medians is not None and selected_category in medians.index:
                        median_val = medians[selected_category]

                    # pick a game counter column
                    game_col = next((c for c in ("Gcar", "G", "Rk") if c in df.columns), None)
                    if game_col:
                        mask = pd.to_numeric(df[game_col], errors="coerce").notna()
                        s = pd.to_numeric(df.loc[mask, selected_category], errors="coerce").dropna()
                        if not s.empty:
                            s_sorted = s.sort_values(ascending=False).reset_index(drop=True)
                            total = len(s_sorted)

                            ranked_items = []
                            # empirical probability P(X >= v) for each entry
                            for i, v in enumerate(s_sorted, start=1):
                                prob = (s_sorted >= v).sum() / total
                                odds = prob_to_american(prob)
                                ranked_items.append({
                                    "rank": i,
                                    "value": int(v) if float(v).is_integer() else float(v),
                                    "prob": prob,
                                    "odds": odds,
                                    "is_median": (median_val is not None and float(v) == float(median_val))
                                })

    return render_template(
        "index.html",
        medians=medians,
        player_name=player_name,
        selected_season=selected_season,
        selected_category=selected_category,
        years=years,
        ranked_items=ranked_items
    )

if __name__ == "__main__":
    app.run(debug=True)
    