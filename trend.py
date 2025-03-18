import logging
import json
import os
import matplotlib.pyplot as plt
from functions import get_player_statistics
from tabulate import tabulate
from ml_model import predict_performance
from nba_api.stats.endpoints import playergamelog
from helpers import display_trends, parse_statistics  # Import display_trends from helpers.py

TREND_STATS_FILE_TEMPLATE = "trend_stats_{}.json"

def analyze_trends(player_id):
    """Fetch and analyze the last 5 games of a player."""
    try:
        # Fetch player game log (last 5 games)
        gamelog = playergamelog.PlayerGameLog(player_id=player_id, season="2024-25")
        games = gamelog.get_dict()["resultSets"][0]["rowSet"]
        headers = gamelog.get_dict()["resultSets"][0]["headers"]

        # Get the last 5 games (if available)
        last_5_games = games[-5:]  # This will get the last 5 games, if there are that many

        # If there are fewer than 5 games, just use all available games
        if len(last_5_games) < 5:
            print(f"Warning: Only {len(last_5_games)} games available for trend analysis.")
        
        # Format the data for parsing
        formatted_games = [dict(zip(headers, game)) for game in last_5_games]
        
        print("Formatted Games:", formatted_games)  # Add logging for debugging
        
        trends, table = parse_statistics(formatted_games)
        
        # Check if trends are properly populated
        if not isinstance(trends, dict):
            raise ValueError("Trends data structure is invalid. Expected a dictionary.")

        # Display trends and table
        create_table(table)
        display_trends(trends)

        # Create the trend graphs for points, assists, rebounds, blocks, and steals
        create_trend_graphs(trends)

    except Exception as e:
        print(f"Error while analyzing trends: {e}")
        logging.error(f"Error while analyzing trends: {e}", exc_info=True)

def create_table(table):
    """Create a table to display the trends in the console."""
    headers = ["Points", "Assists", "Rebounds", "Blocks", "Steals"]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    input("\nPress Enter to continue...")

def create_trend_graphs(trends):
    """Generate graphs for player trends over the last 5 games and an overlay plot."""
    try:
        # First figure: Individual trend graphs
        fig, ax = plt.subplots(3, 2, figsize=(12, 10))  # 3 rows, 2 columns for the plots

        # Points graph
        ax[0, 0].plot(trends["points"], marker='o', color='b', label='Points')
        ax[0, 0].set_title('Points per Game')
        ax[0, 0].set_xlabel('Game')
        ax[0, 0].set_ylabel('Points')

        # Assists graph
        ax[0, 1].plot(trends["assists"], marker='o', color='g', label='Assists')
        ax[0, 1].set_title('Assists per Game')
        ax[0, 1].set_xlabel('Game')
        ax[0, 1].set_ylabel('Assists')

        # Rebounds graph
        ax[1, 0].plot(trends["rebounds"], marker='o', color='r', label='Rebounds')
        ax[1, 0].set_title('Rebounds per Game')
        ax[1, 0].set_xlabel('Game')
        ax[1, 0].set_ylabel('Rebounds')

        # Blocks graph
        ax[1, 1].plot(trends["blocks"], marker='o', color='c', label='Blocks')
        ax[1, 1].set_title('Blocks per Game')
        ax[1, 1].set_xlabel('Game')
        ax[1, 1].set_ylabel('Blocks')

        # Steals graph
        ax[2, 0].plot(trends["steals"], marker='o', color='m', label='Steals')
        ax[2, 0].set_title('Steals per Game')
        ax[2, 0].set_xlabel('Game')
        ax[2, 0].set_ylabel('Steals')

        # Remove empty subplot
        fig.delaxes(ax[2, 1])

        plt.tight_layout()
        plt.show()

        # Second figure: Overlay plot
        plt.figure(figsize=(10, 6))
        games = range(1, len(trends["points"]) + 1)  # Game indices

        # Overlay all statistics
        plt.plot(games, trends["points"], marker='o', color='b', label='Points')
        plt.plot(games, trends["assists"], marker='o', color='g', label='Assists')
        plt.plot(games, trends["rebounds"], marker='o', color='r', label='Rebounds')
        plt.plot(games, trends["blocks"], marker='o', color='c', label='Blocks')
        plt.plot(games, trends["steals"], marker='o', color='m', label='Steals')

        plt.title('Player Performance Trends Overlaid')
        plt.xlabel('Game')
        plt.ylabel('Statistics')
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Error while generating trend graphs: {e}")
        logging.error(f"Error while generating trend graphs: {e}", exc_info=True)