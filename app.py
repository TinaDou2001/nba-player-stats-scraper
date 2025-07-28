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
    years = list(range(current_year, 2000, -1))

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

if __name__ == "__main__":
    app.run(debug=True)