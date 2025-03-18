from sklearn.linear_model import LinearRegression
import numpy as np

def predict_performance(stats):
    """Train a model and predict future performance for points, assists, rebounds, blocks, and steals."""
    # Prepare features and labels from the past stats
    features = np.array([[game["AST"], game["REB"], game["BLK"], game["STL"]] for game in stats])  # Using AST, REB, BLK, STL as features
    labels_points = np.array([game["PTS"] for game in stats])  # Labels for points (PTS)
    labels_assists = np.array([game["AST"] for game in stats])  # Labels for assists (AST)
    labels_rebounds = np.array([game["REB"] for game in stats])  # Labels for rebounds (REB)
    labels_blocks = np.array([game["BLK"] for game in stats])  # Labels for blocks (BLK)
    labels_steals = np.array([game["STL"] for game in stats])  # Labels for steals (STL)

    # Initialize and train models for each statistic (PTS, AST, REB, BLK, STL)
    model_points = LinearRegression()
    model_points.fit(features, labels_points)

    model_assists = LinearRegression()
    model_assists.fit(features, labels_assists)

    model_rebounds = LinearRegression()
    model_rebounds.fit(features, labels_rebounds)

    model_blocks = LinearRegression()
    model_blocks.fit(features, labels_blocks)

    model_steals = LinearRegression()
    model_steals.fit(features, labels_steals)

    # Now, use the most recent game's stats to predict future performance
    latest_game = stats[-1]
    latest_features = np.array([[latest_game["AST"], latest_game["REB"], latest_game["BLK"], latest_game["STL"]]])

    predicted_points = model_points.predict(latest_features)[0]
    predicted_assists = model_assists.predict(latest_features)[0]
    predicted_rebounds = model_rebounds.predict(latest_features)[0]
    predicted_blocks = model_blocks.predict(latest_features)[0]
    predicted_steals = model_steals.predict(latest_features)[0]

    return {
        "points": predicted_points,
        "assists": predicted_assists,
        "rebounds": predicted_rebounds,
        "blocks": predicted_blocks,
        "steals": predicted_steals
    }