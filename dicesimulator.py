#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Dominik Vogel

Projekt: Würfelsimulation

In diesem Projekt simuliere ich das Werfen eines fairen Würfels, um den theoretischen Erwartungswert 
eines Würfels zu überprüfen. Ziel ist es, die geworfenen Augenzahlen zu sammeln, ihren Mittelwert 
zu berechnen und diesen mit dem Erwartungswert von 3,5 zu vergleichen.

### Ablauf meines Programms:
1. Ich simuliere N Würfe eines fairen Würfels.
2. Die Ergebnisse der Würfe speichere ich in einer Liste.
3. Anschließend berechne ich den Mittelwert der geworfenen Augenzahlen.
4. Ich vergleiche den berechneten Mittelwert mit dem theoretischen Erwartungswert von 3,5.
5. Schließlich analysiere ich, wie sich der Mittelwert nähert, wenn ich die Anzahl der Würfe (N) erhöhe oder verringere.

### Hinweise zur Implementierung:
- Ich verwende die Funktion `randint` aus dem `random`-Modul, um die Würfe zu simulieren:
  `from random import randint`.
- Mit dem Befehl `wurf = randint(1, 6)` generiere ich eine zufällige Augenzahl zwischen 1 und 6.
- Den empirischen Mittelwert berechne ich, indem ich die Summe aller Würfe durch die Anzahl der Würfe (N) teile.

Dieses Projekt ermöglicht es mir, das Verhalten eines fairen Würfels zu simulieren und die statistischen Grundlagen 
der Erwartungswerte besser zu verstehen.

## Beispiel

===============================================
WÜRFELSIMULATOR 3000
===============================================
Wie viele Würfe sollen simuliert werden?
10000
===============================================
Simuliere 10000 Würfe...
===============================================
Berechneter Mittelwert: 3.511
Theoretischer Mittelwert: 3.5
===============================================
Noch einmal? (j/n) 

"""

from random import randint

def simulate_dice_rolls(n, dice_rolles):
    """
    
    Simuliert N Würfe eines fairen Würfels und fügt die Ergebnisse der Liste hinzu.

    Anzahl der zu simulierenden Würfe
    dice_rolles: Die Liste, in der alle Wurfergebnisse gespeichert werden
    Der empirische Mittelwert der bisherigen Würfe
    
    """
    # Simulieret n Würfe und füget Ergebnisse zur Liste hinzu
    for _ in range(n):
        wurf = randint(1, 6)  # Generieret eine zufällige Zahl zwischen 1 und 6
        dice_rolles.append(wurf)

    # Berechnet Mittelwert aller bisherigen Würfe
    empirical_mean = sum(dice_rolles) / len(dice_rolles)
    return empirical_mean

def main():
    """
    
    Hauptprogramm für die Würfelsimulation.
    
    """
    
    # Liste zur Speicherung aller Würfelergebnisse
    dice_rolles = []

    while True:
        print("===============================================")
        print("WÜRFELSIMULATOR 3000")
        print("===============================================")
        
        try:
            n = int(input("Wie viele Würfe sollen simuliert werden?\n"))
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")
            continue

        print("===============================================")
        print(f"Simuliere {n} Würfe...")
        print("===============================================")

        # Simulieret Würfelwürfe und berechnet Mittelwert
        empirical_mean = simulate_dice_rolls(n, dice_rolles)

        # Zeiget Ergebnisse der Würfe an
        print(f"Ergebnisse der Würfe (letzte 10): {dice_rolles[-10:]} ...")  # Zeigt nur die letzten 10 Würfe an
        print(f"Berechneter Mittelwert: {empirical_mean:.3f}")
        print("Theoretischer Mittelwert: 3.5")
        print("===============================================")

        # Möglichkeit zur erneuten Ausführung der Simulation
        again = input("Noch einmal? (j/n): ").lower()
        if again != 'j':
            break

    # Ausgabe der gesamten Würfe am Ende des Programms
    print("Alle Würfe:", dice_rolles)

if __name__ == "__main__":
    main()
