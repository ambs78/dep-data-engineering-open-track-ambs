Problem Statement: The debate between who is the NBA's GOAT (Greatest Of All Time) is most of the time subjective, and tends to focus on only a few specific stats.
Objective: I want to create an analysis and dashboard that will include comprehensive data to settle the debate and determine the NBA GOAT.

Using NBA Data available online, I will create a comprehensive dashboard that will allow users to analyze and compare overall career statistics between Michael Jordan, Kobe Bryant and Lebron James.
The dashboard will be used compare all available stats including: FGM, FGA, FG_PCT ,FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK ,TOV, PF and PTS.

I will pull the data using python from the NBAs API: nba_api.stats.endpoints import playergamelog.
The data will contain all of the individual games of each player throughout their careers.
I will summarize their season and overall averages then compare the numbers.

Dashboard will mainly have 2 sections:
1) GOAT Calculator -  will show all relevant stats, where the user can vary the weight of each stat/KPI and calculate the overall GOAT Rating to see who wins. The weight of each stat can be varied using a slider to set the value between 1-10, based on how the user thinks of the significance of the stat. This will allow the user to 'play' with the calculator, and see how changing the weight of the stat will impact the overall score in determining the winner.
2) Stats Dashboard - a dashboard where the user can select a stat using a filter and show the trend for each player to compare their trend over their careers, with the x-axis as the season number of their career.

My main audience will be basketball enthusiasts.
The Philippines is very much interested in Basketball, and they will be a good audience to check my project.
