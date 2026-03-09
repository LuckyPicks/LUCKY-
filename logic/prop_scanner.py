from logic.value_calculator import calculate_edge

SHARP_BOOKS = ["pinnacle", "circa"]

def scan_props(games):

    props = []

    for game in games:

        for bookmaker in game["bookmakers"]:

            book = bookmaker["key"]

            for market in bookmaker["markets"]:

                for outcome in market["outcomes"]:

                    player = outcome.get("name")
                    odds = outcome.get("price")

                    if book in SHARP_BOOKS:
                        sharp_odds = odds
                    else:
                        edge = calculate_edge(sharp_odds, odds)

                        if edge > 0.05:
                            props.append({
                                "player": player,
                                "odds": odds,
                                "edge": edge,
                                "book": book
                            })

    return props
