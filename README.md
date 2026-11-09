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

### Step 7: Launch the Interactive GOAT Dashboard

Open the dashboard notebook, `notebooks/nba_goat_dashboard.ipynb`, which reads the processed files created in Step 6 (plus the accolades table described below). Make sure the virtual environment from Step 2 is activated, then start JupyterLab from the repository root:

```bash
jupyter lab notebooks/nba_goat_dashboard.ipynb
```

In JupyterLab, choose **Run > Run All Cells**. The dashboard appears in the cell outputs, and the sliders and charts update live as you interact with them.

* The notebook looks for the game-log CSVs in `../data/processed` and the accolades CSV in `../data/external`, so it works whether you open it from the `notebooks/` folder or from the repository root.
* All required packages (`plotly`, `ipywidgets`, `anywidget`, `jupyterlab`) are already included in `requirements.txt` from Step 3. If you see an `anywidget not found` message, run `pip install anywidget` and restart the kernel. The dashboard still works without it, but the charts redraw more slowly.
* The pinned `pandas==3.0.3` and `numpy==2.5.1` require a recent Python version. The notebook was tested with Python 3.12.
* GitHub cannot render ipywidgets or Plotly JavaScript, so the sliders only work in JupyterLab, Jupyter Notebook 7, VS Code, or GitHub Codespaces. The last notebook cell optionally exports PNG snapshots to `notebooks/assets/` (requires `kaleido` and Chrome).

---

## Interactive GOAT Dashboard (Jupyter Notebook)

The notebook turns the processed data in `data/processed/` into a dark-mode, NBA-themed dashboard comparing **Michael Jordan**, **Kobe Bryant**, and **LeBron James**. It has two main parts.

### Part 1: GOAT Calculator

* **Two levels of weight sliders (1 to 10):** 13 category sliders, plus a slider for each of the 35 individual stats inside those categories. Everything recalculates live as you drag, and a readout beside each slider shows its real share of the final score.
* **13 weighted categories:** 10 are built from the game logs (Scoring, Efficiency, Playmaking, Rebounding, Defense, Ball Security, Winning, Durability, Peak, Consistency) and 3 from the accolades table (Championships, Individual Awards, Honors).
* **8 presets:** Balanced, Pure Scorer, Winner, Trophy Case, Iron Man, Efficiency Nerd, Two-Way Player, and Peak Performance. Moving any slider switches the preset to a "Custom" state.
* **No bonus for a longer career:** total points, total games, and seasons played are intentionally not scored, and All-Star / All-NBA / All-Defensive selections are scored per season played.
* **Live outputs:** GOAT score podium with a written verdict, weighted-contribution breakdown, trophy case, radar chart, and category-winner heatmap.
* **Weight sweep:** pick any category or individual stat and see how each player's score (and the #1 spot) changes as its weight moves from 1 to 10.
* **Robustness check:** a 10,000-scenario Monte Carlo simulation using random category weights and your current stat-level weights.

### Part 2: Career Trend Analysis & Insights

* **Trend explorer:** 15 metrics compared side-by-side across career seasons, with an option to switch between career year and calendar season on the X-axis, plus a 3-season rolling average.
* **Core metrics and heatmap:** small multiples for six key stats and a season-by-season z-score heatmap for each player.
* **Career curves:** cumulative points, games, and field goals with milestone markers, an efficiency-vs-volume scatter plot (animatable by career year), shot-profile evolution, an aging curve, durability / win % / playoff view, and single-game career highs.
* **Title and MVP seasons:** marked on the trend explorer with a triangle (title) and a circle (MVP).
* **9 insight cards:** generated directly from the data (peak seasons, biggest swings, prime length, efficiency trajectory, shot-profile shift, durability, winning, playmaking and rebounding, title seasons vs the rest).

### Accolades Data (External)

Championships, awards, and honors are not available in the game-log data, so they are stored in a separate, editable table:

* **File:** `data/external/player_accolades.csv`
* **Compiled:** 5 Nov 2026, from NBA.com, ESPN, and Wikipedia / Basketball-Reference-based career achievement lists.
* **Fallback:** the same values are embedded in the notebook, but the CSV takes priority if it exists. Edit the CSV to correct or extend any number, then re-run the notebook.
* **Validation:** the notebook checks the table when it loads (for example, that title seasons match the title count).

---

## Methodology & Limitations

* **Combined stats:** statistics combine regular season and playoffs. Per-season points are derived as `2·FGM + 3PM + FTM` and reconciled with the career `PTS_AVE`.
* **Scoring model:** each stat is scaled 0 to 100 against the best of the three players, so results are relative, not absolute. Stats are averaged into category scores using your stat weights, and category scores are combined using your category weights.
* **Accolades are external:** counts come from the compiled table above, not from the game-log CSVs, and voting rules and eligibility have changed over time (for example, LeBron's 2026 All-NBA streak ended under the 65-game minimum).
* **Not included:** advanced metrics (PER, WS, BPM) and player ages are not in the data and were not added.
* **Small sample:** with only three players, every ranking is relative, and the GOAT score is a model of your own priorities rather than an objective truth.
