
"""

@author: Dominik Vogel

# Projekt 7: Tic-Tac-Toe II

## Projektbeschreibung

Ziel dieses Projekts ist es, unser bestehendes Tic-Tac-Toe-Spiel durch Modularisierung 
und die Einführung einer primitiven Künstlichen Intelligenz (KI) zu erweitern. 
Du wirst dein Programm in logische Module aufteilen, um die Übersichtlichkeit und 
Wartbarkeit des Codes zu verbessern. Zusätzlich führst du eine einfache KI ein, 
gegen die gespielt werden kann.

### Module:

- **board.py**: Enthält alle Funktionen, die das Spielbrett betreffen. Refaktorisiere 
dein bisheriges Programm so, dass eine klare Trennung der Funktionalität gegeben ist 
und alle spielfeldbezogenen Funktionen hierunter fallen.
- **KI.py**: Enthält Funktionen, die das Verhalten der KI steuern. Zunächst i
mplementierst du eine Funktion für zufällige Züge der KI.

### Funktionen in board.py:

- `draw_board(position)`: Zeichnet die aktuelle Spielposition.
- `check_if_valid(position, zug)`: Überprüft, ob ein Zug möglich ist.
- `check_win_condition(position)`: Prüft, ob ein Spieler gewonnen hat oder das 
Spiel unentschieden endet.
- `clear_board()`: Initialisiert ein leeres Spielbrett.

### Funktionen in KI.py:

- `make_random_move(position)`: Wählt zufällig ein leeres Feld für den Zug der KI.

### Erweiterung der KI:

Wenn du möchtest, kannst du eine zusätzliche Funktion `make_good_move` entwickeln, 
die intelligentere Züge ermöglicht, um das Spiel herausfordernder zu gestalten.

### Struktur des Programms:

Das Hauptprogramm (`main.py`) integriert die Module und steuert den Spielablauf. 
Es initialisiert das Spielbrett, führt Spieler- und KI-Züge durch und überprüft 
nach jedem Zug den Spielstatus. Die genaue Implementierung kann variieren, sollte 
aber die Modularisierung des Codes und die Interaktion zwischen Spieler und KI berücksichtigen.

### Abgabe:

Das fertige Programm soll als reiner Python-Code mit mehreren Dateien (*.py) 
abgegeben werden, wobei die Funktionen und Module wie beschrieben umgesetzt werden sollen.

"""

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
