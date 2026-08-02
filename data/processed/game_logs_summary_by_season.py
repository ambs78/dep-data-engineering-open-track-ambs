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
output_file = script_dir / "game_logs_summary_per_season.csv"

dfs = []
for filename in files:
    file_path = script_dir / filename

    if file_path.exists():
        df = pd.read_csv(file_path)

        # Remove duplicate column names if any exist in headers
        df = df.loc[:, ~df.columns.duplicated()]

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

    # 2. Run SQL query using DuckDB
    # DuckDB automatically reads 'combined_raw_df' directly as a table
    sql_query = """
        SELECT 
            PLAYER_NAME,
            SEASON_YEAR,
            SUM(CAST(FGA AS FLOAT)) AS TOTAL_FGA,
            SUM(CAST(FGM AS FLOAT)) AS TOTAL_FGM
        FROM combined_raw_df
        WHERE SEASON_YEAR IS NOT NULL
        GROUP BY PLAYER_NAME, SEASON_YEAR
        ORDER BY PLAYER_NAME, SEASON_YEAR ASC
    """

    summary_df = duckdb.sql(sql_query).df()

    # 3. Export the SQL summary result to CSV
    summary_df.to_csv(output_file, index=False)
    print(f"\nSuccess! Aggregated SQL summary saved to: {output_file}")
else:
    print("\nNo CSV files were found. Output CSV was not created.")

input("\nPress Enter to exit...")