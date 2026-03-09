def american_to_probability(odds):

    if odds > 0:
        return 100 / (odds + 100)
    else:
        return -odds / (-odds + 100)


def calculate_edge(sharp_odds, book_odds):

    sharp_prob = american_to_probability(sharp_odds)
    book_prob = american_to_probability(book_odds)

    return sharp_prob - book_prob
