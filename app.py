from datetime import datetime
from flask import Flask, request, render_template
from nba_scraper import get_player_suffix, get_game_log_table, calculate_medians

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    medians = None
    player_name = ""
    selected_season = "2024"
    current_year = datetime.now().year
    years = list(range(current_year, 2003, -1))

    if request.method == "POST":
        player_name = request.form["player_name"]
        selected_season = request.form.get("season", "2024")
        suffix = get_player_suffix(player_name)
        if suffix:
            df = get_game_log_table(suffix, selected_season)
            if df is not None:
                medians = calculate_medians(df)

    return render_template(
        "index.html",
        medians=medians,
        player_name=player_name,
        selected_season=selected_season,
        current_year=current_year,
        years=years
    )

@app.route("/odds", methods=["GET", "POST"])
def odds():
    result = {}
    if request.method == "POST":
        odds_type = request.form.get("odds_type")
        value = request.form.get("value")

        try:
            val = float(value)
            if odds_type == "Decimal":
                implied = 1 / val if val > 1 else 0
                american = (val - 1) * 100 if val >= 2 else -100 / (val - 1)
                fractional = f"{int((val - 1) * 100)}/100"
                decimal = val
            elif odds_type == "American":
                implied = 100 / (val + 100) if val > 0 else -val / (-val + 100)
                decimal = (val / 100 + 1) if val > 0 else (100 / -val + 1)
                fractional = f"{int((decimal - 1) * 100)}/100"
                american = val
            elif odds_type == "Fractional":
                decimal = val + 1
                implied = 1 / decimal
                american = (val * 100) if val >= 1 else -100 / val
                fractional = f"{int(val * 100)}/100"

            result = {
                "implied_prob": round(implied, 4),
                "decimal": round(decimal, 2),
                "american": int(american),
                "fractional": fractional
            }

        except (ValueError, TypeError):
            result = {"error": "Invalid input. Please enter a number."}

    return render_template("odds.html", **result)

if __name__ == "__main__":
    app.run(debug=True)