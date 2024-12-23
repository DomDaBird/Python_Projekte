

import random

def make_random_move(position):
    available_moves = [i for i in range(len(position)) if position[i] == ' ']
    return random.choice(available_moves)

# Optional: smartere KI-Logik
def make_good_move(position, player):
    opponent = 'O' if player == 'X' else 'X'

    # 1. Zuerst versuche zu gewinnen
    for i in range(len(position)):
        if position[i] == ' ':
            position[i] = player
            if check_win_condition(position) == player:
                return i
            position[i] = ' '

    # 2. Blockiere den Gegner, wenn er gewinnen könnte
    for i in range(len(position)):
        if position[i] == ' ':
            position[i] = opponent
            if check_win_condition(position) == opponent:
                position[i] = ' '
                return i
            position[i] = ' '

    # 3. Mach einen zufälligen Zug, wenn kein Gewinnzug oder Block möglich ist
    return make_random_move(position)
