import json
import os
import time
import requests

# Base URL for OpenDota API
BASE_URL = "https://api.opendota.com/api"


def save_json_data(data, filename):
    """Saves the pulled data to a file inside the GitHub repository."""
    os.makedirs("data", exist_ok=True)
    filepath = os.path.join("data", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"✓ Data successfully saved to {filepath}")


def fetch_pro_players():
    """Pulls comprehensive profiles of high-level historical players."""
    print("Fetching player base directories from OpenDota...")
    url = f"{BASE_URL}/proPlayers"
    response = requests.get(url)

    if response.status_code == 200:
        players = response.json()
        save_json_data(players, "pro_players_base.json")
        return players
    else:
        print(f"Error fetching players: {response.status_code}")
        return None


def fetch_player_historical_matches(account_id):
    """Pulls historical match stats for a specific player ID."""
    print(f"Fetching historical match history for player ID: {account_id}...")
    url = f"{BASE_URL}/players/{account_id}/matches"
    params = {"limit": 100}  # Pulls their last 100 historical matches
    response = requests.get(url, params=params)

    if response.status_code == 200:
        matches = response.json()
        save_json_data(matches, f"player_{account_id}_history.json")
    else:
        print(f"Error fetching match history: {response.status_code}")


if __name__ == "__main__":
    # 1. Fetch a broad player base list
    player_base = fetch_pro_players()

    if player_base:
        # 2. Pick a prominent sample player from the base to extract deep history
        sample_player_id = player_base[0].get("account_id")

        # OpenDota's free tier allows 5 requests/minute. Respect the rate limit.
        time.sleep(2)

        if sample_player_id:
            # 3. Pull their historical stats
            fetch_player_historical_matches(sample_player_id)