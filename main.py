from functions import initialize_player_cache, search_player, get_player_statistics
from helpers import display_trends, display_game_info
from ml_model import predict_performance
from trend import analyze_trends, create_trend_graphs
import json
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, filename="error_log.txt", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    try:
        print("Welcome to the NBA Player Statistics Analyzer!")

        # Initialize player cache
        initialize_player_cache()

        player_name = input("Enter the player's name (first, last, or full): ").strip()

        player = search_player(player_name)
        if not player:
            print("Player not found. Please try again.")
            return

        print(f"Selected Player: {player['first_name']} {player['last_name']}")

        # Ask if the user wants to analyze trends
        action = input("Do you want to analyze trends for this player? (yes/no): ").strip().lower()
        if action == 'yes':
            analyze_trends(player['id'])
        
        # Alternatively, fetch player stats if needed
        stats = get_player_statistics(player["id"])
        if not stats:
            print(f"No statistics found for {player['first_name']} {player['last_name']}.")
            return

        # Fetch formatted games and display them in a table
        formatted_games = stats if isinstance(stats, list) else stats.get('games', [])
        if formatted_games:  # If there are games data
            display_game_info(formatted_games)  # Display games in table format
        else:
            print("No game data available for this player.")

        display_trends(stats)

        predictions = predict_performance(stats)
        print("\nPredicted Performance:")
        print(json.dumps(predictions, indent=4))

    except Exception as e:
        print("\nAn error occurred. Check 'error_log.txt' for details.")
        logging.error("An unexpected error occurred.", exc_info=True)

if __name__ == "__main__":
    main()
