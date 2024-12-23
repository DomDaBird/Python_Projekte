
"""
@author: Dominik Vogel

Projekt: Schere-Stein-Papier

### Projektbeschreibung

In diesem Projekt entwickle ich ein Schere-Stein-Papier-Spiel, bei dem ich gegen den Computer antrete. Sowohl ich als auch der Computer wählen gleichzeitig eine der folgenden Optionen:
- Schere
- Stein
- Papier
- (optional: Brunnen)

Je nach Kombination gibt es unterschiedliche Ergebnisse:

| Teilnehmende | Schere          | Stein            | Papier           |
|--------------|-----------------|------------------|------------------|
| Schere       | Unentschieden   | Stein gewinnt    | Schere gewinnt   |
| Stein        | Stein gewinnt   | Unentschieden    | Papier gewinnt   |
| Papier       | Schere gewinnt  | Papier gewinnt   | Unentschieden    |

### Spielablauf

1. Ich werde über die Konsole aufgefordert, zwischen Schere, Stein und Papier zu wählen. Es besteht auch die Möglichkeit, das Spiel zu beenden.
2. Bei Spielabbruch wird der Punktestand ausgegeben und das Spiel beendet.
3. Wähle ich eine Option, simuliert der Computer eine zufällige Auswahl.
4. Der Gewinner der Runde wird ermittelt und die Punkte werden entsprechend vergeben.
5. Nach jeder Runde wird der aktuelle Punktestand angezeigt.
6. Das Spiel läuft so lange, bis ich mich entscheide, es zu beenden.

### Simulation der Computerwahl

Der Computer trifft seine Wahl zufällig, um ein faires Spiel zu gewährleisten. Hierfür nutze ich die Funktion `randint(a, b)` aus dem Python-Modul `random`, die eine ganze Zahl zwischen `a` und `b` (inklusive) erzeugt.  
Die Zuordnung könnte wie folgt aussehen:
- 1 für Stein
- 2 für Schere
- 3 für Papier  

"""

from random import randint

def get_computer_choice():
    """
    
    Simuliert die Wahl des Computers.
    
    Eine Zufallswahl aus 'Stein', 'Schere', 'Papier'
    
    """
    choices = ['Stein', 'Schere', 'Papier']
    return choices[randint(0, 2)]

def determine_winner(player_choice, computer_choice):
    
    """
    
    Bestimmt den Gewinner zwischen dem Spieler und dem Computer.
    
    player_choice: Die Wahl des Spielers ('Stein', 'Schere' oder 'Papier')
    computer_choice: Die Wahl des Computers ('Stein', 'Schere' oder 'Papier')
    Ein String, der den Gewinner anzeigt oder 'Unentschieden'
    
    """
    if player_choice == computer_choice:
        return "Unentschieden"
    
    if (player_choice == 'Schere' and computer_choice == 'Papier') or \
       (player_choice == 'Stein' and computer_choice == 'Schere') or \
       (player_choice == 'Papier' and computer_choice == 'Stein'):
        return "Spieler gewinnt"
    
    return "Computer gewinnt"

def play_game():
    
    """
    Startet das Schere-Stein-Papier-Spiel.
    """
    
    player_score = 0
    computer_score = 0
    
    print("Willkommen zum Schere-Stein-Papier-Spiel!")
    print("Du kannst wählen: Stein, Schere oder Papier.")
    print("Um das Spiel zu beenden, tippe 'Beenden'.")
    
    while True:
        # Spieler wählt Option
        player_choice = input("Deine Wahl: ").capitalize()
        
        if player_choice == 'Beenden':
            break
        
        if player_choice not in ['Stein', 'Schere', 'Papier']:
            print("Ungültige Eingabe. Bitte wähle Stein, Schere oder Papier.")
            continue
        
        # Computer wählt eine Option
        computer_choice = get_computer_choice()
        print(f"Computer wählt: {computer_choice}")
        
        # Bestimmt Gewinner
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        # Aktualisiert Punktestand
        if result == "Spieler gewinnt":
            player_score += 1
        elif result == "Computer gewinnt":
            computer_score += 1
        
        # Ausgabe aktueller Punktestand
        print(f"Punktestand - Spieler: {player_score}, Computer: {computer_score}")
    
    print("Spiel beendet.")
    print(f"Endgültiger Punktestand - Spieler: {player_score}, Computer: {computer_score}")

# Hauptprogramm ausführen
if __name__ == "__main__":
    play_game()

