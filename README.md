**Problem Statement**: The debate between who is the NBA's GOAT (Greatest Of All Time) is most of the time subjective, and tends to focus on only a few specific stats.


**Objective**: I want to create an analysis and dashboard that will include comprehensive data to settle the debate and determine the NBA GOAT.


Using NBA Data available online, I will create a comprehensive dashboard that will allow users to analyze and compare overall career statistics between Michael Jordan, Kobe Bryant and Lebron James.
The dashboard will be used compare all available stats including: FGM, FGA, FG_PCT ,FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK ,TOV, PF and PTS.


**Primary Source**
_NBA API_: (nba_api.stats.endpoints.playergamelog)
_URL_: https://github.com/swar/nba_api
_Format_: JSON / Python API endpoint (pandas DataFrame response)
_Coverage_: Individual game-by-game statistics for Michael Jordan, Kobe Bryant, and LeBron James across their entire regular season and playoff careers.
_Why it fits the problem_: Provides official, granular, real-time accessible game log data directly from NBA Stats, enabling precise calculations for career and seasonal statistical comparisons.
_Known limitations_: Rate limits and occasional connection timeouts when querying the official NBA API endpoints; requires error handling and request delays.

**Fallback Source**
_Kaggle NBA Dataset_ (Michael Jordan, Kobe Bryant, and LeBron James Stats)
_URL_: https://www.kaggle.com/datasets/xvivancos/michael-jordan-kobe-bryant-and-lebron-james-stats
_Format_: CSV
_Coverage_: Historical career game logs and statistics for Michael Jordan, Kobe Bryant, and LeBron James.
_Why it fits the problem_: Serves as a reliable offline backup containing pre-extracted game log data in case the live nba_api endpoint experiences downtime or rate-limiting issues.
_Known limitations_: Static dataset that is not automatically updated with current-season games or live updates.


**Dashboard Sections**
1) GOAT Calculator -  will show all relevant stats, where the user can vary the weight of each stat/KPI and calculate the overall GOAT Rating to see who wins. The weight of each stat can be varied using a slider to set the value between 1-10, based on how the user thinks of the significance of the stat. This will allow the user to 'play' with the calculator, and see how changing the weight of the stat will impact the overall score in determining the winner.
2) Stats Dashboard - a dashboard where the user can select a stat using a filter and show the trend for each player to compare their trend over their careers, with the x-axis as the season number of their career.

My main audience will be basketball enthusiasts.
The Philippines is very much interested in Basketball, and they will be a good audience to check my project.
