from nba_api.stats.endpoints import playergamelog
import json
import os

CACHE_FILE = "players_cache.json"
STATS_FILE_TEMPLATE = "stats_{}.json"  # Template for saving stats (e.g., stats_203507.json)

def initialize_player_cache():
    """Fetch all players and cache only first_name, last_name, and id."""
    if os.path.exists(CACHE_FILE):
        return

    print("Initializing player cache...")
    from nba_api.stats.static import players  # Import here to reduce startup time
    all_players = players.get_players()
    formatted_players = [{"id": p["id"], "first_name": p["first_name"], "last_name": p["last_name"]} for p in all_players]

    with open(CACHE_FILE, "w") as cache_file:
        json.dump(formatted_players, cache_file, indent=4)
    print("Player cache initialized.")

def search_player(player_name):
    """Search for players by name and return matching options."""
    with open(CACHE_FILE, "r") as cache_file:
        player_cache = json.load(cache_file)

    matches = [
        player for player in player_cache
        if player_name.lower() in (player["first_name"].lower() + " " + player["last_name"].lower()) or
        player_name.lower() in player["first_name"].lower() or
        player_name.lower() in player["last_name"].lower()
    ]

    if not matches:
        return None

    if len(matches) == 1:
        return matches[0]

    print("\nMultiple players found:")
    for i, player in enumerate(matches, start=1):
        print(f"{i}. {player['first_name']} {player['last_name']}")

    while True:
        try:
            choice = int(input("Select the player by entering the corresponding number: "))
            if 1 <= choice <= len(matches):
                return matches[choice - 1]
        except ValueError:
            pass
        print("Invalid choice. Please try again.")

def get_player_statistics(player_id):
    """Fetch player statistics and save them to a JSON file."""
    stats_file = STATS_FILE_TEMPLATE.format(player_id)

    if os.path.exists(stats_file):
        print("Statistics already cached. Loading from file...")
        with open(stats_file, "r") as file:
            return json.load(file)

    print("Fetching player statistics...")
    try:
        gamelog = playergamelog.PlayerGameLog(player_id=player_id, season="2024-25")
        stats = gamelog.get_dict()["resultSets"][0]["rowSet"]
        headers = gamelog.get_dict()["resultSets"][0]["headers"]

        formatted_stats = [
            dict(zip(headers, game)) for game in stats
        ]

        with open(stats_file, "w") as file:
            json.dump(formatted_stats, file, indent=4)

        print(f"Statistics saved to {stats_file}.")
        return formatted_stats
    except Exception as e:
        print(f"Failed to fetch statistics: {e}")
        return None
