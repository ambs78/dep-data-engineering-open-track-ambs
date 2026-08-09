from pathlib import Path
import duckdb
import pandas as pd

# Get the directory where THIS script is currently saved
script_dir = Path(__file__).parent.resolve()

files = [
    "kobe_bryant_game_logs.csv",
    "lebron_james_game_logs.csv",
    "michael_jordan_game_logs.csv",
]

# Output path definitions
output_file_season = script_dir / "game_logs_summary_per_season.csv"
output_file_career = script_dir / "game_logs_summary_career_overall.csv"

dfs = []
for filename in files:
    file_path = script_dir / filename

    if file_path.exists():
        df = pd.read_csv(file_path)

        # Ensure column headers are uppercase for consistent SQL querying
        df.columns = df.columns.str.upper()

        # Derive clean player name from filename
        formatted_name = (
            file_path.stem.replace("_game_logs", "").replace("_", " ").title()
        )

        # Set or update the PLAYER_NAME column
        df["PLAYER_NAME"] = formatted_name

        dfs.append(df)
        print(f"Loaded: {filename}")
    else:
        print(f"Warning: Could not find {filename} at {file_path}")

if dfs:
    # 1. Combine raw logs in pandas
    combined_raw_df = pd.concat(dfs, ignore_index=True)

    # 2. Run SQL query using DuckDB: Stats per Season
    sql_query_per_season = """
        SELECT 
            PLAYER_NAME
            ,SEASON_YEAR

            -- Assign a Sequence Number to each player's season
            ,ROW_NUMBER() OVER (PARTITION BY PLAYER_NAME ORDER BY SEASON_YEAR ASC) AS PLAYER_SEASON_NUM

            -- Games Played
            ,COUNT(DISTINCT GAME_ID) AS GAMES_PLAYED_TOTAL
            ,COUNT(DISTINCT GAME_ID) FILTER (WHERE SEASON_TYPE = 'Regular Season') AS GAMES_PLAYED_REGULAR_SEASON
            ,COUNT(DISTINCT GAME_ID) FILTER (WHERE SEASON_TYPE = 'Playoffs')       AS GAMES_PLAYED_PLAYOFFS
            ,COUNT(DISTINCT GAME_ID) FILTER (WHERE SEASON_TYPE = 'Regular Season' AND WL = 'W') AS REGULAR_SEASON_WINS
            ,CAST(COUNT(DISTINCT GAME_ID) FILTER (WHERE SEASON_TYPE = 'Regular Season' AND WL = 'W') AS FLOAT) / NULLIF(COUNT(DISTINCT GAME_ID) FILTER (WHERE SEASON_TYPE = 'Regular Season'), 0) AS REGULAR_SEASON_WIN_PCT

            -- Field Goals
            ,SUM(CAST(FGA AS FLOAT)) AS TOTAL_FGA
            ,SUM(CAST(FGM AS FLOAT)) AS TOTAL_FGM
            ,SUM(CAST(FGM AS FLOAT)) / NULLIF(SUM(CAST(FGA AS FLOAT)), 0) AS TOTAL_FG_PCT

            -- 3 Points
            ,SUM(CAST(FG3A AS FLOAT)) AS TOTAL_FG3A
            ,SUM(CAST(FG3M AS FLOAT)) AS TOTAL_FG3M
            ,SUM(CAST(FG3M AS FLOAT)) / NULLIF(SUM(CAST(FG3A AS FLOAT)), 0) AS TOTAL_FG3_PCT

            -- Free Throws
            ,SUM(CAST(FTA AS FLOAT)) AS TOTAL_FTA
            ,SUM(CAST(FTM AS FLOAT)) AS TOTAL_FTM
            ,SUM(CAST(FTM AS FLOAT)) / NULLIF(SUM(CAST(FTA AS FLOAT)), 0) AS TOTAL_FT_PCT

            -- Average Stats
            ,AVG(CAST(OREB AS FLOAT)) AS OREB_AVE
            ,AVG(CAST(DREB AS FLOAT)) AS DREB_AVE
            ,AVG(CAST(REB AS FLOAT)) AS REB_AVE
            ,AVG(CAST(AST AS FLOAT)) AS AST_AVE
            ,AVG(CAST(STL AS FLOAT)) AS STL_AVE
            ,AVG(CAST(BLK AS FLOAT)) AS BLK_AVE
            ,AVG(CAST(TOV AS FLOAT)) AS TOV_AVE
            ,AVG(CAST(PF AS FLOAT)) AS FOULS_AVE
            ,COUNT(PF) FILTER (WHERE CAST(PF AS FLOAT) = 6) AS FOULED_OUT_TOTAL

        FROM combined_raw_df
        WHERE SEASON_YEAR IS NOT NULL
        GROUP BY PLAYER_NAME, SEASON_YEAR
        ORDER BY PLAYER_NAME, SEASON_YEAR ASC
    """

    summary_season_df = duckdb.sql(sql_query_per_season).df()

    # 3. Export the Season SQL summary result to CSV
    summary_season_df.to_csv(output_file_season, index=False)
    print(f"\nSuccess! Aggregated Season summary saved to: {output_file_season}")

    # 4. Run SQL query using DuckDB: Stats per Overall Career
    sql_query_career_overall = """
        SELECT 
            PLAYER_NAME

            -- Games Played
            ,COUNT(DISTINCT GAME_ID) AS GAMES_PLAYED_TOTAL
            ,COUNT(DISTINCT SEASON_YEAR) AS TOTAL_SEASONS_PLAYED
            ,COUNT(DISTINCT SEASON_ID) FILTER (WHERE SEASON_TYPE = 'Playoffs') AS TOTAL_PLAYOFF_SEASONS_PLAYED
            ,COUNT(DISTINCT GAME_ID) FILTER (WHERE SEASON_TYPE = 'Regular Season') AS GAMES_PLAYED_REGULAR_SEASON
            ,COUNT(DISTINCT GAME_ID) FILTER (WHERE SEASON_TYPE = 'Playoffs')       AS GAMES_PLAYED_PLAYOFFS
            ,COUNT(DISTINCT GAME_ID) FILTER (WHERE SEASON_TYPE = 'Regular Season' AND WL = 'W') AS REGULAR_SEASON_WINS
            ,CAST(COUNT(DISTINCT GAME_ID) FILTER (WHERE SEASON_TYPE = 'Regular Season' AND WL = 'W') AS FLOAT) / NULLIF(COUNT(DISTINCT GAME_ID) FILTER (WHERE SEASON_TYPE = 'Regular Season'), 0) AS REGULAR_SEASON_WIN_PCT

            -- Field Goals
            ,SUM(CAST(FGA AS FLOAT)) AS TOTAL_FGA
            ,SUM(CAST(FGM AS FLOAT)) AS TOTAL_FGM
            ,SUM(CAST(FGM AS FLOAT)) / NULLIF(SUM(CAST(FGA AS FLOAT)), 0) AS TOTAL_FG_PCT

            -- 3 Points
            ,SUM(CAST(FG3A AS FLOAT)) AS TOTAL_FG3A
            ,SUM(CAST(FG3M AS FLOAT)) AS TOTAL_FG3M
            ,SUM(CAST(FG3M AS FLOAT)) / NULLIF(SUM(CAST(FG3A AS FLOAT)), 0) AS TOTAL_FG3_PCT

            -- Free Throws
            ,SUM(CAST(FTA AS FLOAT)) AS TOTAL_FTA
            ,SUM(CAST(FTM AS FLOAT)) AS TOTAL_FTM
            ,SUM(CAST(FTM AS FLOAT)) / NULLIF(SUM(CAST(FTA AS FLOAT)), 0) AS TOTAL_FT_PCT

            -- Average Stats
            ,AVG(CAST(PTS AS FLOAT)) AS PTS_AVE
            ,AVG(CAST(OREB AS FLOAT)) AS OREB_AVE
            ,AVG(CAST(DREB AS FLOAT)) AS DREB_AVE
            ,AVG(CAST(REB AS FLOAT)) AS REB_AVE
            ,AVG(CAST(AST AS FLOAT)) AS AST_AVE
            ,AVG(CAST(STL AS FLOAT)) AS STL_AVE
            ,AVG(CAST(BLK AS FLOAT)) AS BLK_AVE
            ,AVG(CAST(TOV AS FLOAT)) AS TOV_AVE
            ,AVG(CAST(PF AS FLOAT)) AS FOULS_AVE
            ,COUNT(PF) FILTER (WHERE CAST(PF AS FLOAT) = 6) AS FOULED_OUT_TOTAL

            -- Career Highs
            ,MAX(CAST(PTS AS FLOAT)) AS PTS_MAX
            ,MAX(CAST(OREB AS FLOAT)) AS OREB_MAX
            ,MAX(CAST(DREB AS FLOAT)) AS DREB_MAX
            ,MAX(CAST(REB AS FLOAT)) AS REB_MAX
            ,MAX(CAST(AST AS FLOAT)) AS AST_MAX
            ,MAX(CAST(STL AS FLOAT)) AS STL_MAX
            ,MAX(CAST(BLK AS FLOAT)) AS BLK_MAX
            ,MAX(CAST(TOV AS FLOAT)) AS TOV_MAX

        FROM combined_raw_df
        WHERE SEASON_YEAR IS NOT NULL
        GROUP BY PLAYER_NAME
    """

    summary_career_df = duckdb.sql(sql_query_career_overall).df()

    # 5. Export the Career SQL summary result to CSV
    summary_career_df.to_csv(output_file_career, index=False)
    print(f"Success! Aggregated Career summary saved to: {output_file_career}")

else:
    print("\nNo CSV files were found. Output CSV files were not created.")

input("\nPress Enter to exit...")
