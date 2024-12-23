"""

@author: Dominik Vogel

Projekt: Hangman mit Python und SQLite

### Projektbeschreibung
In diesem Projekt programmiere ich das klassische Spiel **Hangman**. Dabei wählt der Computer ein zufälliges Wort 
aus einer **SQLite-Datenbank (database.db)** aus. Der Spieler muss dieses Wort erraten, indem er einzelne Buchstaben wählt. 
Hierbei hat der Spieler nur eine begrenzte Anzahl an Versuchen.

Zusätzlich erstelle ich ein Programm, das es ermöglicht, neue Wörter in die Datenbank hinzuzufügen.

---

### Die Datenbank
Die **SQLite-Datenbank database.db** enthält eine Tabelle namens `words` mit zwei Spalten:
- **word**: Das Wort selbst.
- **letters**: Die Anzahl der Buchstaben des Wortes.

Alle Wörter in der Datenbank sind in **Großbuchstaben** gespeichert, um die Unterscheidung zwischen Groß- und Kleinschreibung zu vermeiden.

Beispielhafte Struktur der Tabelle:
| word     | letters |
|----------|---------|
| KATZE    | 5       |
| BOOT     | 4       |
| MAUS     | 4       |
| HAUSBOOT | 8       |
| UHR      | 3       |

---

### Funktionalitäten des Spiels

Der Ablauf meines Programms umfasst folgende Schritte:
1. Herstellung einer Verbindung zur **SQLite-Datenbank**.
2. Verwendung von **SQL-Abfragen**, um Wörter einer bestimmten Länge aus der Datenbank auszuwählen.
3. Zufällige Auswahl eines Wortes aus den Abfrageergebnissen.
4. Interaktion mit dem Spieler über die Konsole, um das Wort zu erraten.
5. Beenden des Spiels, wenn der Spieler die maximale Anzahl an Versuchen aufgebraucht hat.

Mit diesen Funktionen baue ich ein vollständig interaktives Spiel, das den Spieler fordert und zusätzlich eine einfache Verwaltung der Wörter über die Datenbank ermöglicht.


"""

import sqlite3
import random

# Datenbank-Verbindung herstellen
def connect_db():
    return sqlite3.connect('database.db')

# Tabelle erstellen, falls noch nicht existiert
def create_table(connection):
    with connection:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS words (
                word TEXT PRIMARY KEY,
                letters INTEGER
            )
        ''')

# Neues Wort zur Datenbank hinzufügen
def add_word(connection, word):
    word = word.upper()
    letters = len(word)
    with connection:
        connection.execute("INSERT INTO words (word, letters) VALUES (?, ?)", (word, letters))

# Wort einer bestimmten Länge zufällig auswählen
def get_random_word(connection, length):
    cur = connection.cursor()
    cur.execute("SELECT word FROM words WHERE letters = ?", (length,))
    words = cur.fetchall()
    if words:
        return random.choice(words)[0]
    return None

# Verfügbare Wortlängen herausfinden
def get_available_word_lengths(connection):
    cur = connection.cursor()
    cur.execute("SELECT DISTINCT letters FROM words ORDER BY letters")
    return [row[0] for row in cur.fetchall()]

# Hangman-Spiel
def play_hangman():
    connection = connect_db()
    create_table(connection)
    
    available_lengths = get_available_word_lengths(connection)
    
    if not available_lengths:
        print("Die Datenbank enthält keine Wörter.")
        return
    
    print(f"Verfügbare Wortlängen: {', '.join(map(str, available_lengths))}")
    
    while True:
        try:
            length = int(input("Wähle die Anzahl der Buchstaben für das gesuchte Wort: "))
            if length in available_lengths:
                break
            else:
                print(f"Bitte wähle eine der verfügbaren Längen: {', '.join(map(str, available_lengths))}")
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")
    
    word = get_random_word(connection, length)
    
    if not word:
        print("Kein Wort mit dieser Länge gefunden!")
        return
    
    guessed = "_" * length
    attempts = 5
    guessed_letters = set()
    
    while attempts > 0 and guessed != word:
        print(f"Gesuchtes Wort: {guessed}")
        guess = input("Rate einen Buchstaben: ").upper()
        
        if guess in guessed_letters:
            print("Buchstabe bereits geraten!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            guessed = "".join([letter if letter == guess else guessed[i] for i, letter in enumerate(word)])
        else:
            attempts -= 1
            print(f"Falsch! Noch {attempts} Versuche übrig.")
    
    if guessed == word:
        print(f"Glückwunsch! Du hast das Wort '{word}' erraten.")
    else:
        print(f"Verloren! Das Wort war '{word}'.")

    connection.close()

# Wörter zur Datenbank hinzufügen
def add_words_to_db():
    connection = connect_db()
    create_table(connection)
    
    while True:
        word = input("Gib ein neues Wort ein (oder 'q' zum Beenden): ")
        if word.lower() == 'q':
            break
        add_word(connection, word)
        print(f"Das Wort '{word.upper()}' wurde hinzugefügt.")
    
    connection.close()

# Hauptmenü, das nach jeder Aktion zurückkehrt
def main_menu():
    while True:
        print("\n1: Hangman spielen")
        print("2: Wörter zur Datenbank hinzufügen")
        print("3: Beenden")
        choice = input("Wähle eine Option: ")
        
        if choice == "1":
            play_hangman()
        elif choice == "2":
            add_words_to_db()
        elif choice == "3":
            print("Programm beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Auswahl! Bitte versuche es erneut.")

# Hauptprogramm
if __name__ == "__main__":
    main_menu()
