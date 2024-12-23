
def draw_board(position):
    print(f"""
     {position[0]} | {position[1]} | {position[2]} 
    -----------
     {position[3]} | {position[4]} | {position[5]} 
    -----------
     {position[6]} | {position[7]} | {position[8]} 
    """)

def check_if_valid(position, zug):
    return position[zug] == ' '

def check_win_condition(position):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontale
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertikale
        [0, 4, 8], [2, 4, 6]              # Diagonale
    ]
    for condition in win_conditions:
        if position[condition[0]] == position[condition[1]] == position[condition[2]] != ' ':
            return position[condition[0]]
    
    if ' ' not in position:
        return 'Unentschieden'
    
    return None

def clear_board():
    return [' '] * 9
