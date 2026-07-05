import time
import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players

# 1. Define the players and their exact career spans to minimize empty requests
PLAYERS_META = {
    "Michael Jordan": {
        "id": "893",
        "start_year": 1984,
        "end_year": 2003
    },
    "Kobe Bryant": {
        "id": "977",
        "start_year": 1996,
        "end_year": 2016
    },
    "LeBron James": {
        "id": "2544",
        "start_year": 2003,
        "end_year": 2026  # Captures up to the most recent 2025-26 season
    }
}

def generate_season_string(year):
    """Converts an integer year like 1996 to NBA format '1996-97'"""
    next_year = str(year + 1)[-2:]
    return f"{year}-{next_year}"

def fetch_career_game_logs():
    all_players_data = []

    for name, info in PLAYERS_META.items():
        print(f"Starting data pull for {name}...")
        player_games = []
        
        # Loop through every season of their career
        for year in range(info["start_year"], info["end_year"] + 1):
            season_str = generate_season_string(year)
            
            # Extract both Regular Season and Playoffs
            for season_type in ["Regular Season", "Playoffs"]:
                try:
                    print(f"  Fetching {season_str} ({season_type})...")
                    
                    # Call NBA API endpoint
                    gamelog = playergamelog.PlayerGameLog(
                        player_id=info["id"],
                        season=season_str,
                        season_type_all_star=season_type
                    )
                    
                    df = gamelog.get_data_frames()[0]
                    
                    if not df.empty:
                        # Annotate data with context columns you'll need for analysis
                        df["PLAYER_NAME"] = name
                        df["SEASON_TYPE"] = season_type
                        df["SEASON_YEAR"] = season_str
                        player_games.append(df)
                        
                except Exception as e:
                    print(f"    Skipped or errored out for {season_str} {season_type}: {e}")
                
                # Respectful pacing to prevent getting rate-limited/blocked by NBA.com
                time.sleep(1.5)
        
        if player_games:
            # Combine individual player's seasons
            player_master_df = pd.concat(player_games, ignore_index=True)
            
            # Save individual copy for your backup
            filename = f"{name.lower().replace(' ', '_')}_game_logs.csv"
            player_master_df.to_csv(filename, index=False)
            print(f"✔ Successfully saved {len(player_master_df)} rows to {filename}\n")
            
            all_players_data.append(player_master_df)
            
    # Combine everyone into a single master file for easier side-by-side EDA
    if all_players_data:
        master_df = pd.concat(all_players_data, ignore_index=True)
        master_df.to_csv("goat_comparison_master_gamelogs.csv", index=False)
        print("🎉 Master file 'goat_comparison_master_gamelogs.csv' generated perfectly!")

if __name__ == "__main__":
    fetch_career_game_logs()