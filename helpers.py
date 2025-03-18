from tabulate import tabulate
import matplotlib.pyplot as plt

def parse_statistics(stats):
    """Parse statistics to extract trends and create a table for display."""
    trends = {"points": [], "assists": [], "rebounds": [], "blocks": [], "steals": []}
    table = []

    for game in stats:
        points = game.get("PTS", 0)
        assists = game.get("AST", 0)
        rebounds = game.get("REB", 0)
        blocks = game.get("BLK", 0)
        steals = game.get("STL", 0)

        # We will just use a placeholder for GAME_ID if missing, or exclude it completely if not needed
        game_id = game.get("GAME_ID", "N/A")  # If GAME_ID is important later, you can handle it in another way.

        trends["points"].append(points)
        trends["assists"].append(assists)
        trends["rebounds"].append(rebounds)
        trends["blocks"].append(blocks)
        trends["steals"].append(steals)

        # Append stats to table (excluding GAME_ID for now)
        table.append([points, assists, rebounds, blocks, steals])

    return trends, table

def display_game_info(formatted_games):
    """Display formatted game information in a tabular format."""
    headers = ['Game Date', 'Matchup', 'WL', 'Minutes', 'FG%', '3P%', 'FT%', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Plus/Minus']
    table_data = []

    for game in formatted_games:
        # Extract relevant game data
        game_data = [
            game.get("GAME_DATE", "N/A"),
            game.get("MATCHUP", "N/A"),
            game.get("WL", "N/A"),
            game.get("MIN", 0),
            game.get("FG_PCT", 0),
            game.get("FG3_PCT", 0),
            game.get("FT_PCT", 0),
            game.get("REB", 0),
            game.get("AST", 0),
            game.get("STL", 0),
            game.get("BLK", 0),
            game.get("TOV", 0),
            game.get("PF", 0),
            game.get("PTS", 0),
            game.get("PLUS_MINUS", 0)
        ]
        table_data.append(game_data)

    # Print the table
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    input("\nPress Enter to continue...")

def display_trends(trends):
    """Display a summary of trends for key statistics."""
    if isinstance(trends, dict):  # Ensure trends is a dictionary
        print("\n--- Player Performance Trends ---")
        print(f"Total Points: {sum(trends['points'])}")
        print(f"Average Points per Game: {sum(trends['points']) / len(trends['points']):.2f}")
        print(f"Total Assists: {sum(trends['assists'])}")
        print(f"Average Assists per Game: {sum(trends['assists']) / len(trends['assists']):.2f}")
        print(f"Total Rebounds: {sum(trends['rebounds'])}")
        print(f"Average Rebounds per Game: {sum(trends['rebounds']) / len(trends['rebounds']):.2f}")
        print(f"Total Blocks: {sum(trends['blocks'])}")
        print(f"Average Blocks per Game: {sum(trends['blocks']) / len(trends['blocks']):.2f}")
        print(f"Total Steals: {sum(trends['steals'])}")
        print(f"Average Steals per Game: {sum(trends['steals']) / len(trends['steals']):.2f}")
    # If trends are unavailable, do nothing