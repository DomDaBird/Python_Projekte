"""

@author: Dominik Vogel

Projekt: Tic-Tac-Toe II

In diesem Projekt erweitere ich mein bestehendes Tic-Tac-Toe-Spiel durch Modularisierung 
und die Einführung einer primitiven Künstlichen Intelligenz (KI). Mein Ziel ist es, den 
Code in logische Module zu unterteilen, um Übersichtlichkeit und Wartbarkeit zu verbessern, 
und eine einfache KI zu implementieren, gegen die gespielt werden kann.

### Module:

- **board.py**: Dieses Modul enthält alle Funktionen, die das Spielbrett betreffen. 
  Ich refaktorisiere mein bestehendes Programm so, dass alle spielfeldbezogenen Funktionen 
  in diesem Modul gekapselt sind.
- **KI.py**: Hier implementiere ich Funktionen, die das Verhalten der KI steuern. 
  Zunächst baue ich eine Funktion für zufällige Züge der KI ein.

### Funktionen in board.py:

- `draw_board(position)`: Zeichnet die aktuelle Spielposition auf dem Spielfeld.
- `check_if_valid(position, zug)`: Überprüft, ob ein Zug gültig ist.
- `check_win_condition(position)`: Prüft, ob ein Spieler gewonnen hat oder ob das 
  Spiel unentschieden endet.
- `clear_board()`: Initialisiert ein leeres Spielfeld.

### Funktionen in KI.py:

- `make_random_move(position)`: Führt einen zufälligen Zug für die KI aus.

### Erweiterung der KI:

Zusätzlich kann ich eine Funktion `make_good_move` entwickeln, die intelligentere 
Züge ermöglicht, um die KI für den Spieler herausfordernder zu machen.

### Struktur des Programms:

Das Hauptprogramm (`main.py`) integriert die Module und steuert den Spielablauf. 
Es initialisiert das Spielfeld, führt Spieler- und KI-Züge aus und überprüft nach 
jedem Zug den Spielstatus. Dabei achte ich darauf, die Module klar zu trennen und 
eine einfache Interaktion zwischen Spieler und KI zu gewährleisten.

"""

# main.py

import board
import KI

def play_game():
    position = board.clear_board()
    current_player = 'X'

    while True:
        board.draw_board(position)

        if current_player == 'X':
            try:
                zug = int(input("Wähle dein Feld (1-9): ")) - 1  # Umrechnung von 1-9 auf 0-8
                if zug not in range(9):
                    raise ValueError
                if not board.check_if_valid(position, zug):
                    print("Ungültiger Zug, das Feld ist bereits belegt. Bitte versuche es erneut.")
                    continue
            except ValueError:
                print("Ungültige Eingabe, bitte eine Zahl zwischen 1 und 9 eingeben.")
                continue
        else:
            print("Die KI macht ihren Zug...")
            zug = KI.make_random_move(position)

        position[zug] = current_player

        result = board.check_win_condition(position)
        if result:
            board.draw_board(position)
            if result == 'Unentschieden':
                print("Das Spiel endet unentschieden!")
            else:
                print(f"Spieler {result} gewinnt!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
