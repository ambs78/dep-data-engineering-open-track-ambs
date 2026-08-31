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
git clone [https://github.com/ambs78/dep-data-engineering-open-track-ambs.git](https://github.com/ambs78/dep-data-engineering-open-track-ambs.git)
cd dep-data-engineering-open-track-ambs