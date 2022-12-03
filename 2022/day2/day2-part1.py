def score_for_scissors(round_results: list):
    if round_results[0] == 'A':
        return 0
    if round_results[0] == 'B':
        return 6
    if round_results[0] == 'C':
        return 3


def score_for_paper(round_results: list):
    if round_results[0] == 'A':
        return 6
    if round_results[0] == 'B':
        return 3
    if round_results[0] == 'C':
        return 0


def score_for_rock(round_results: list):
    if round_results[0] == 'A':
        return 3
    elif round_results[0] == 'B':
        return 0
    elif round_results[0] == 'C':
        return 6


def tournament_score(tournament_moves) -> int:
    total_score = 0
    for round in tournament_moves:
        round_results = (list(round.replace(" ", "")))
        if round_results[1] == 'X':
            total_score += score_for_rock(round_results) + 1
        if round_results[1] == 'Y':
            total_score += score_for_paper(round_results) + 2
        if round_results[1] == 'Z':
            total_score += score_for_scissors(round_results) + 3
    return total_score

tournament_moves = open("input.txt", "r")
print(f"Your total score for the tournament is {tournament_score(tournament_moves)}")
