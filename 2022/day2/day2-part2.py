def score_for_scissors(round_results: list):
    if round_results[1] == 'X':
        return 0 + 2
    elif round_results[1] == 'Y':
        return 3 + 3
    elif round_results[1] == 'Z':
        return 6 + 1


def score_for_paper(round_results: list):
    if round_results[1] == 'X':
        return 0 + 1
    elif round_results[1] == 'Y':
        return 3 + 2
    elif round_results[1] == 'Z':
        return 6 + 3


def score_for_rock(round_results: list):
    if round_results[1] == 'X':
        return 0 + 3
    elif round_results[1] == 'Y':
        return 3 + 1
    elif round_results[1] == 'Z':
        return 6 + 2


def tournament_score(tournament_moves) -> int:
    total_score = 0
    for round in tournament_moves:
        round_results = (list(round.replace(" ", "")))
        if round_results[0] == 'A':
            total_score += score_for_rock(round_results)
        if round_results[0] == 'B':
            total_score += score_for_paper(round_results)
        if round_results[0] == 'C':
            total_score += score_for_scissors(round_results)
    return total_score

tournament_moves = open("input.txt", "r")
print(f"Your total score for the tournament is {tournament_score(tournament_moves)}")