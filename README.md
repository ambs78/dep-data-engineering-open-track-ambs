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

Open the dashboard notebook, `notebooks/nba_goat_dashboard.ipynb`. It reads the processed files created in Step 6 together with the accolades table described below. Make sure the virtual environment from Step 2 is activated, then start JupyterLab from the repository root:

```bash
jupyter lab notebooks/nba_goat_dashboard.ipynb
```

JupyterLab opens in your default web browser (usually at `http://localhost:8888/lab`). If it does not open automatically, copy the URL printed in the terminal (it ends with `?token=...`) into your browser, and keep the terminal window open while you work. Once the notebook is open, choose **Run > Run All Cells** from the menu bar at the top. The dashboard appears in the cell outputs, and the charts, sliders, and scoreboard update live as you interact with them.

* The notebook looks for the game-log CSVs in `../data/processed` and the accolades CSV in `../data/external`, so it works whether you open it from the `notebooks/` folder or from the repository root.
* The packages it needs (`plotly`, `ipywidgets`, `jupyterlab`) are included in `requirements.txt` from Step 3.
* The pinned `pandas==3.0.3` and `numpy==2.5.1` require a recent Python version. The notebook was tested with Python 3.12.
* GitHub cannot render ipywidgets or Plotly JavaScript, so the sliders and charts only work in JupyterLab, Jupyter Notebook 7, VS Code, or GitHub Codespaces.

---

## Interactive GOAT Dashboard (Jupyter Notebook)

The notebook turns the processed data into a dark-mode, NBA-themed dashboard comparing **Michael Jordan**, **Kobe Bryant**, and **LeBron James**. It has two sections: a Trend Explorer and a GOAT Calculator.

| Section | Data source |
|---|---|
| Trend Explorer | `data/processed/game_logs_summary_per_season.csv` (title and MVP markers use `data/external/player_accolades.csv`) |
| GOAT Calculator | `data/processed/game_logs_summary_career_overall.csv` and `data/external/player_accolades.csv` |

### Section 1: Trend Explorer

Compare how each career evolved, season by season, for any metric.

* **Metric dropdown:** 15 metrics, including points, True Shooting %, field goal %, 3-point %, free throw %, assists, rebounds, steals, blocks, turnovers, 3-point attempts, free-throw attempts, games played, and win %.
* **Controls:** choose which players to show, switch the X-axis between career year (rookies line up at year 1) and calendar season, add a 3-season rolling average, and toggle the title (triangle) and MVP (circle) season markers.
* **Chart conventions:** a star marks each player's best season for the chosen metric, hollow markers flag seasons with fewer than 30 games, and a broken line marks a calendar gap in the data (such as a retirement).
* **The Scoreboard (right side):** an insights table that compares the players against each other on the chosen metric, written with a bit of attitude. It covers best single season, typical season, steadiness, glow-up or fade, a year-by-year bracket (same career year versus same career year), above-the-pack seasons, and championship mode (title seasons versus all other seasons). The headline names the winner of the most categories and awards a playful "belt" such as *Bucket Boss* or *Safe Hands Champion*.
* **Live and data-driven:** the scoreboard recalculates whenever you change the metric or the selected players. It uses qualifying seasons only (30 or more games), and every number in it is computed from the data.

### Section 2: GOAT Calculator

Decide what "greatest" means to you by weighting 15 rows: 9 career stats and 6 accolades.

* **Career stats:** Field Goal %, 3-Point %, Free Throw %, Points per Game, Rebounds per Game, Assists per Game, Steals per Game, Blocks per Game, and Turnovers per Game (fewer is better).
* **Accolades:** NBA Championships, Finals MVP Awards, League MVP Awards, Defensive Player of the Year, Scoring Titles, and All-NBA 1st Team Selections.
* **Weight sliders (1 to 10):** each row has its own slider, and a readout shows that row's share of the total score. Everything recalculates live as you drag, and a **Reset weights** button returns every slider to 5.
* **Three numbers per player, per row:**
  * **Career:** the actual figure from the data.
  * **Normalized:** the career figure scored 0 to 100 against the best of the three players.
  * **Weighted Score:** the normalized score multiplied by the row's share of the total weight.
* **GOAT ranking and total:** each player's card at the top shows their rank and Total Weighted Score (the sum of their weighted scores), and the table repeats the totals at the bottom.
* **Best-in-row highlight:** the best performer in each row has their Career, Normalized, and Weighted Score cells outlined in their player color (for turnovers, the lowest value wins).
* **Built-in explanation:** a "How the weighted scores are normalized and calculated" panel under the table includes a worked example that updates with your sliders.
* **No bonus for a longer career:** total points, total games, and seasons played are intentionally not used.

**How the scoring works**

1. Normalized score = `career value / best value x 100` (for turnovers: `best value / career value`), so the leader in every row scores 100.
2. Share of the weight = `your slider value / sum of all 15 slider values`.
3. Weighted score = `normalized score x share`.
4. Total Weighted Score = the sum of a player's weighted scores. The highest total is GOAT #1.

**Player headshots (optional)**

The calculator shows each player's initials by default. To add photos, save images you have the right to use in `notebooks/assets/headshots/` using these file names (`.png`, `.jpg`, `.jpeg`, or `.webp`), then re-run the notebook:

* `michael_jordan.jpg`
* `kobe_bryant.jpg`
* `lebron_james.jpg`

**Customizing the calculator**

To add, remove, or swap rows (for example, use All-Star selections instead of Scoring Titles), edit the `CALC_ROWS` list in the GOAT Calculator cell of the notebook.

### Accolades Data (External)

Championships, awards, and honors are not available in the game-log data, so they are stored in a separate, editable table:

* **File:** `data/external/player_accolades.csv`
* **Compiled:** 5 Nov 2026, from NBA.com, ESPN, and Wikipedia / Basketball-Reference-based career achievement lists.
* **Fallback:** the same values are embedded in the notebook, but the CSV takes priority if it exists. Edit the CSV to correct or extend any number, then re-run the notebook.
* **Validation:** the notebook checks the table when it loads (for example, that the listed title seasons match the title count and exist in the season data).

---

## Methodology & Limitations

* **Combined stats:** statistics combine regular season and playoffs. Per-season points are derived as `2*FGM + 3PM + FTM` and reconciled with the career `PTS_AVE` when the notebook loads.
* **Normalization:** each row is scaled 0 to 100 against the best of the three players, so results are relative, not absolute. This compresses near-ties (for example, free-throw %), so rows with small real gaps still look close.
* **Weighting:** sliders from 1 to 10 become shares of the total weight, so the shares always add up to 100%. With equal weights, the 6 accolade rows make up 40% of the score, so lowering their sliders shows how much the ranking depends on accolades.
* **Accolades are external:** counts come from the compiled table above, not from the game-log CSVs. Voting rules and eligibility have changed over time (for example, LeBron's 2026 All-NBA streak ended under the league's 65-game minimum), and counts such as Finals MVPs depend on teammates and opponents.
* **Playful insights:** the Trend Explorer commentary is generated from the data using fixed templates. It is meant to be fun, not definitive.
* **Not included:** advanced metrics (PER, WS, BPM) and player ages are not in the data and were not added.
* **Small sample:** with only three players, every ranking is relative, and the GOAT score is a model of your own priorities rather than an objective truth.
