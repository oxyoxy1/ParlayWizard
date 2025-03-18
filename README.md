# ParlayWizard

ParlayWizard is an NBA stat-tracking companion designed to help you analyze player performance for your parlays. It provides real-time statistics, trends, and machine learning predictions to help you make informed decisions.

## Features
- **Player Search:** Easily look up NBA players and retrieve their latest stats.
- **Trend Analysis:** Track player performance over recent games.
- **Graphical Insights:** Visualize trends with interactive charts.
- **Machine Learning Predictions:** Get estimated points, assists, rebounds, and blocks.
- **User-Friendly Interface:** Simple menu-driven navigation.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/oxyoxy1/ParlayWizard.git
   ```
2. Navigate to the project folder:
   ```sh
   cd ParlayWizard
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the main program with:
```sh
python main.py
```
Follow the on-screen prompts to search for players and analyze their stats.

## File Structure
- `main.py` - Handles user interaction and visualization.
- `functions.py` - Processes statistical analysis and trend calculations.
- `helpers.py` - Retrieves data from the Balldontlie API.
- `ml_model.py` - Runs machine learning predictions.
- `trend.py` - Makes trend predictions.

## Dependencies
- Python 3.8+
- Pandas
- Matplotlib
- Scikit-learn
- Requests
- nba-api

## Future Enhancements
- Live game tracking
- Expanded machine learning models
- Customizable alerts for player performance

## License
This project is licensed under the MIT License.

## Contributions
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## Contact
For questions or feedback, reach out via GitHub issues.
