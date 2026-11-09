# NBA GOAT Analysis & Interactive Dashboard

## Problem Statement

The debate over who is the NBA's GOAT (Greatest Of All Time) is often subjective and tends to focus on only a few selective statistics.

## Objective

This project creates a comprehensive analysis and interactive dashboard to compare career statistics and help determine the NBA GOAT.

Using data extracted from official sources, the dashboard allows users to analyze and compare granular career stats between **Michael Jordan**, **Kobe Bryant**, and **LeBron James**.

The dashboard includes key metrics across regular season and playoff careers, including:
`FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, and `PTS`.

---

## Data Sources

### Primary Source: NBA API

* **Endpoint:** `nba_api.stats.endpoints.playergamelog`
* **URL:** [https://github.com/swar/nba_api](https://github.com/swar/nba_api)
* **Format:** JSON / Python API endpoint (pandas DataFrame response)
* **Coverage:** Individual game-by-game statistics for Michael Jordan, Kobe Bryant, and LeBron James across their entire regular season and playoff careers.
* **Why it fits:** Provides official, granular game log data directly from NBA Stats, enabling precise statistical calculations.
* **Known limitations:** Rate limits and occasional connection timeouts requiring request delays and error handling.

### Fallback Source: Kaggle NBA Dataset

* **Dataset:** Michael Jordan, Kobe Bryant, and LeBron James Stats
* **URL:** [https://www.kaggle.com/datasets/xvivancos/michael-jordan-kobe-bryant-and-lebron-james-stats](https://www.kaggle.com/datasets/xvivancos/michael-jordan-kobe-bryant-and-lebron-james-stats)
* **Format:** CSV
* **Coverage:** Historical career game logs for all three players.
* **Why it fits:** Serves as a reliable offline backup if the live `nba_api` endpoint experiences downtime or rate limits.
* **Known limitations:** Static dataset that is not automatically updated with live games.

---

## Dashboard Features

1. **GOAT Calculator:** Allows users to assign weights (from 1 to 10) to each statistical KPI using interactive sliders. The calculator dynamically recalculates each player's custom overall score based on the user's weighting preference.
2. **Stats Dashboard:** Enables users to select specific statistics and compare player trends side-by-side across their respective career seasons (using career season number on the X-axis).

---

## Getting Started & Execution

Follow these steps to set up your environment, install the required packages, and run the data ingestion pipeline.

### Prerequisites

* Python 3.8 or higher installed on your system.
* Git installed on your system.

### Step 1: Clone and Navigate to the Repository

Open your terminal (Command Prompt, PowerShell, or Terminal) and clone the repository, then navigate into your local project directory:

```bash
git clone https://github.com/ambs78/dep-data-engineering-open-track-ambs.git
cd dep-data-engineering-open-track-ambs
```

### Step 2: Create and Activate a Virtual Environment

Isolate your Python dependencies by creating a virtual environment named `.venv`:

```bash
python -m venv .venv
```

Activate the environment based on your operating system:

**Windows (Command Prompt):**
```bat
.venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

### Step 3: Install Required Modules

Install all required Python packages from the `requirements.txt` file into your virtual environment:

```bash
pip install -r requirements.txt
```

### Step 4: Export Python Dependencies (Optional Maintenance)

If you install new packages while developing, you can freeze and update the `requirements.txt` file by running:

```bash
pip freeze > requirements.txt
```

### Step 5: Run Data Ingestion

Execute the `ingest.py` script located in the `scripts/` folder to fetch and process player statistics:

```bash
python scripts/ingest.py
```

### Step 6: Transform the Data

Execute the `transform.py` script located in the `scripts/` folder to fetch and process player statistics.
This will combine the data from the 3 players, ang get their career averages for `FGM`, `FGA`, `FG_PCT`, `FG3M`, `FG3A`, `FG3_PCT`, `FTM`, `FTA`, `FT_PCT`, `OREB`, `DREB`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, and `PTS`.

This will be the data that will be used in creating the Main GOAT Dashboard and Calculator.

```bash
python scripts/transform.py
```

Interactive GOAT Dashboard (Jupyter Notebook)
`notebooks/nba\_goat\_dashboard.ipynb` turns the processed files in `data/processed/` into a dark-mode, NBA-themed dashboard comparing Michael Jordan, Kobe Bryant and LeBron James.
Part 1 · GOAT Calculator
Two levels of weight sliders, both on a 1–10 scale: 13 category sliders plus a slider for each of the 35 individual stats. Everything updates live as you drag, and a readout shows each slider's real share of the final score
13 weighted categories and 8 presets (plus a "Custom" state when you move a slider): 10 from the game logs (Scoring, Efficiency, Playmaking, Rebounding, Defense, Ball Security, Winning, Durability, Peak, Consistency) plus 3 from an accolades table (Championships, Individual Awards, Honors)
Career-volume totals (total points, total games, seasons played) are not scored, so the longest career gets no automatic edge; All-Star/All-NBA/All-Defensive selections are scored per season played
Live GOAT score podium, weighted-contribution breakdown, trophy case, radar chart and category-winner heatmap
Weight sweep: pick any category or individual stat and see how the GOAT scores (and the #1 spot) change as its weight goes 1 → 10
10,000-scenario Monte Carlo robustness check that uses your current stat-level weights
Part 2 · Career Trend Analysis & Insights
Trend explorer (15 metrics), core-metric small multiples, season-by-season z-score heatmap
Cumulative career curves with milestones, efficiency-vs-volume scatter (animatable), shot-profile shift, aging curve, durability/win%/playoff view, single-game career highs
Title (▲) and MVP (○) seasons marked on the trend explorer
9 insight cards generated from the data (peak seasons, biggest swings, prime length, efficiency trajectory, shot-profile shift, durability, winning, playmaking/rebounding, title seasons vs the rest)
Run it
```bash
# from the repo root, with the .venv from Step 2 activated
pip install -r requirements.txt
jupyter lab notebooks/nba\_goat\_dashboard.ipynb      # then: Run > Run All Cells
```
The notebook looks for the game-log CSVs in `../data/processed` and the accolades CSV in `../data/external`, so run it from the `notebooks/` folder (the default when opened from JupyterLab or VS Code).
> \*\*Viewing note:\*\* GitHub does not render ipywidgets or Plotly JavaScript. Interactivity works in JupyterLab, Jupyter Notebook 7, VS Code and Codespaces. The last notebook cell exports PNG snapshots to `notebooks/assets/` (needs `kaleido` + Chrome).
Methodology & limitations
Stats combine regular season and playoffs; per-season points are derived as `2·FGM + 3PM + FTM` and reconciled with the career `PTS\_AVE`.
Scores are scaled 0–100 against the best of the three players for each sub-metric, so results are relative, not absolute.
Championships, awards and honours are not in the game-log CSVs. They come from `data/external/player\_accolades.csv` (compiled 5 Nov 2026 from NBA.com, ESPN and Wikipedia/Basketball-Reference-based lists; the same values are embedded in the notebook as a fallback). Edit that CSV to correct or extend them.
Advanced metrics (PER, WS, BPM) and ages are not in the data and were not added.
