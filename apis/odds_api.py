import requests

API_KEY = "cfae3c955efd39b619bec6fee8945580"

def fetch_nba_odds():

    url = "https://api.the-odds-api.com/v4/sports/basketball_nba/odds"

    params = {
        "apiKey": API_KEY,
        "regions": "us",
        "markets": "player_points,player_assists,player_rebounds",
        "oddsFormat": "american"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

    return None
