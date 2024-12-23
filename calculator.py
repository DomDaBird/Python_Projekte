#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Dominik Vogel

Projekt: Einfacher Taschenrechner

In diesem Projekt entwickle ich einen einfachen Taschenrechner, der auf Benutzereingaben reagiert 
und verschiedene mathematische Operationen ausführt.

### Ablauf meines Programms:
1. Ich fordere den Benutzer auf, eine erste Gleitkommazahl einzugeben.
2. Danach lasse ich den Benutzer einen mathematischen Operator auswählen.
   Unterstützte Operatoren sind: +, −, ×, /, //, %, **.
3. Anschließend frage ich eine zweite Gleitkommazahl ab.
4. Nach Eingabe aller Daten berechne ich das Ergebnis und gebe es in der Konsole aus.
5. Zuletzt erscheint eine Eingabeaufforderung, mit der der Benutzer wählen kann, 
   ob er eine weitere Berechnung durchführen möchte.

Der Taschenrechner bietet so eine einfache Möglichkeit, grundlegende mathematische Operationen 
direkt auszuführen und mehrfach hintereinander zu verwenden.

## Beispiel

===============================================
Guten Tag!
Ich bin der beste Taschenrechner!
Ich kann +, −, ×, /, //, % und ** berechnen!
===============================================
Tippe die erste Zahl ein...                  5
Was willst du mit dieser Zahl tun?           +
Tippe die zweite Zahl ein...                 7
===============================================
Das Ergebnis der Rechnung 5 + 7 lautet 12 ! 
===============================================
Noch einmal? (j/n) 


"""

def calculator():
    print("===============================================")
    print()
    print("Guten Tag!")
    print("Ich bin der beste Taschenrechner!")
    print("Ich kann +, −, ×, /, //, % und ** berechnen!")
    print()
    print("===============================================")

    while True:
        try:
            # Erste Zahl
            first_number = float(input("Tippe die erste Zahl ein: "))

            # Überprüfung des Operators
            valid_operators = ["+", "-", "*", "/", "//", "%", "**"]
            while True:
                operator = input("Was willst du mit dieser Zahl tun? (+, −, *, /, //, %, **): ")
                if operator in valid_operators:
                    break
                else:
                    print("Ungültiger Operator. Bitte wähle einen der folgenden: +, −, *, /, //, %, **")

            # Zweite Zahl
            second_number = float(input("Tippe die zweite Zahl ein: "))

            # Berechnung nach Wahl Operator
            if operator == "+":
                result = first_number + second_number
            elif operator == "-":
                result = first_number - second_number
            elif operator == "*":
                result = first_number * second_number
            elif operator == "/":
                if second_number != 0:
                    result = first_number / second_number
                else:
                    print("Fehler: Division durch Null ist nicht erlaubt.")
                    continue
            elif operator == "//":
                if second_number != 0:
                    result = first_number // second_number
                else:
                    print("Fehler: Ganzzahlige Division durch Null ist nicht erlaubt.")
                    continue
            elif operator == "%":
                if second_number != 0:
                    result = first_number % second_number
                else:
                    print("Fehler: Modulo-Division durch Null ist nicht erlaubt.")
                    continue
            elif operator == "**":
                result = first_number ** second_number

            # Ausgabe des Ergebnisses
            print("===============================================")
            print(f"Das Ergebnis der Rechnung {first_number} {operator} {second_number} lautet {result}!")
            print("===============================================")

        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
            continue

        # Abfrage, ob der Benutzer eine weitere Berechnung durchführen möchte
        repeat = input("Noch einmal? (j/n): ").strip().lower()
        if repeat != 'j':
            print("Auf Wiedersehen!")
            break

# Hauptprogramm

print("+ ist Addition")
print("- ist Subtraktion")
print("* ist Multiplikation")
print("/ ist Division")
print("// ganzzahlige Division")
print("% ist der Restwert")
print("** ist Exponentiation")

if __name__ == "__main__":
    calculator()



