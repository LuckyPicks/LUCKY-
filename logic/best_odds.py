def get_best_odds(props):

    best_lines = []

    for game in props:

        if "bookmakers" not in game:
            continue

        for bookmaker in game["bookmakers"]:

            book = bookmaker["title"]

            for market in bookmaker["markets"]:

                for outcome in market["outcomes"]:

                    best_lines.append({
                        "player": outcome["name"],
                        "line": outcome.get("point"),
                        "odds": outcome["price"],
                        "book": book
                    })

    return best_lines