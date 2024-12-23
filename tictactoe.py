#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Dominik Vogel

Projekt: Tic-Tac-Toe

In diesem Projekt entwickle ich ein Tic-Tac-Toe-Spiel, das über die Konsole gespielt wird. 
Zwei Spieler können nacheinander ein oder mehrere Spiele gegeneinander spielen. Das Spielbrett 
besteht aus einem 3x3-Feld, und die Spieler setzen abwechselnd ihre Steine auf freie Felder, 
indem sie die Nummer des Feldes eingeben. Ein Spieler gewinnt, wenn er drei seiner Steine 
in einer horizontalen, vertikalen oder diagonalen Reihe platziert. Das Spielfeld wird klar und 
übersichtlich in der Konsole dargestellt.

### Anforderungen:
1. **Spielbrettdarstellung**: 
   - Das Spielbrett ist ein 3x3-Feld, dessen Felder von oben links beginnend durchnummeriert sind. 
   - Ich stelle das Spielbrett durch eine Ausgabe in der Konsole dar.
2. **Spieleraktionen**: 
   - Die Spieler geben abwechselnd die Nummer des Feldes ein, auf dem sie ihren Stein setzen möchten. 
   - Ihre Züge werden sofort auf dem Spielfeld sichtbar.
3. **Spiellogik**: 
   - Nach jedem Zug prüfe ich, ob ein Spieler gewonnen hat (drei gleiche Steine in einer Reihe, Spalte oder Diagonale).
4. **Spielende**: 
   - Das Spiel endet, wenn ein Spieler gewinnt oder alle Felder belegt sind, ohne dass ein Gewinner feststeht.

### Struktur des Programms:
Das Programm läuft in einer Schleife, die das Spiel fortsetzt, bis ein Spieler gewinnt 
oder es unentschieden endet. Dabei:
- Zeichne ich das Spielfeld nach jedem Zug.
- Fordere ich die Spieler abwechselnd auf, ihre Züge einzugeben.
- Prüfe ich, ob der Zug gültig ist und ob ein Spieler gewonnen hat.

### Wesentliche Funktionen:
- `draw_board(position)`: Zeichnet das Spielbrett in der Konsole.
- `check_if_valid(position, move)`: Überprüft, ob ein Zug gültig ist.
- `check_win_condition(position)`: Überprüft, ob ein Spieler gewonnen hat.

"""

def draw_board(board):
    """
    Zeichnet aktuelles Spielbrett in Konsole.
    """
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_if_valid(board, move):
    """
    Überprüft, ob Zug gültig ist.
    """
    if board[move] == ' ':
        return True
    return False

def check_win_condition(board):
    """
    Überprüft, ob Spieler gewonnen hat.
    """
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontale Reihen
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertikale Spalten
                      (0, 4, 8), (2, 4, 6)]  # diagonale Reihen
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    return None

def is_board_full(board):
    """
    Überprüft, ob Spielbrett voll ist.
    """
    return ' ' not in board

def get_valid_move(board, current_player):
    """
    Fordert den Spieler zur Eingabe eines gültigen Zuges auf.
    """
    while True:
        try:
            move = int(input(f"Player {current_player}, wo soll gesetzt werden? [0-8]: "))
            if 0 <= move <= 8:  # Überprüfen, ob die Eingabe im gültigen Bereich liegt
                if check_if_valid(board, move):  # Überprüfen, ob das Feld frei ist
                    return move
                else:
                    print("Das Feld ist bereits belegt. Bitte wähle ein anderes Feld.")
            else:
                print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 0 und 8 ein.")
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 0 und 8 ein.")

def main():
    """
    Hauptprogramm
    """
    board = [' ' for _ in range(9)]
    players = ['X', 'O']
    current_player = 0

    while True:
        draw_board(board)
        move = get_valid_move(board, players[current_player])
        
        board[move] = players[current_player]
        winner = check_win_condition(board)
        
        if winner:
            draw_board(board)
            print(f"Spieler {winner} hat gewonnen!")
            break
        
        if is_board_full(board):
            draw_board(board)
            print("Unentschieden!")
            break
        
        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    main()
