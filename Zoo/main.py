"""

@author: Dominik Vogel


Projekt: Zoo-Verwaltungssystem

In diesem Projekt entwickle ich ein Zoo-Verwaltungssystem mithilfe der 
Objektorientierten Programmierung (OOP) in Python. Ziel ist es, verschiedene 
Tierklassen zu erstellen und dabei Konzepte wie Klassen, Instanzen und 
Vererbung praktisch anzuwenden. Dieses Projekt hilft mir, OOP in Python zu vertiefen.

### Struktur meines Programms:

Das System besteht aus mehreren Dateien, die verschiedene Tierklassen 
und ein Hauptprogramm umfassen:

- **main.py**: Hier initialisiere ich die verschiedenen Tierinstanzen und interagiere mit ihnen.
- **tier.py**: Diese Datei enthält die Basisklasse `Tier`, von der alle spezifischen 
  Tierklassen erben.
- **tiger.py**: Beinhaltet die spezifische Klasse `Tiger`, die von `Tier` erbt.
- **gorilla.py**: Beinhaltet die spezifische Klasse `Gorilla`, die von `Tier` erbt.
- ...weitere Tierklassen nach Bedarf...

### Die Basisklasse `Tier`:

Die Basisklasse `Tier` bildet die Grundlage für alle Tiere und enthält:

- **Instanzattribute**:
  - `name`: Der Name des Tieres (String).
  - `sex`: Das Geschlecht des Tieres (Boolean: `0` für männlich, `1` für weiblich).
  - `age`: Das Alter des Tieres (Integer).

- **Methoden**:
  - `eat()`: Gibt eine Nachricht aus, dass das Tier isst (z.B. "Max isst.").
  - `sleep()`: Gibt eine Nachricht aus, dass das Tier schläft (z.B. "Max schläft.").
  - `grow(years)`: Erhöht das Alter des Tieres um `years` Jahre und gibt eine 
    Nachricht aus (z.B. "Max wurde 5 Jahre älter und ist jetzt 20 Jahre alt.").

### Die Kindklassen:

Jede Kindklasse erbt von der Basisklasse `Tier` und implementiert zusätzliche 
spezifische Eigenschaften und Methoden:

- **Klassenattribute**:
  - `num_appendages`: Die Anzahl der Extremitäten (Integer).
  - `is_cold_blooded`: Gibt an, ob das Tier kaltblütig ist (Boolean).
  - `is_mammal`: Gibt an, ob das Tier ein Säugetier ist (Boolean).

- **Überschriebene Methoden**:
  - Angepasste Nachrichten für `eat()`, `sleep()`, und `grow(years)`.

- **Spezifische Methoden**:
  - Jede Kindklasse erhält einzigartige Funktionen, z.B. `klettern()` für die Gorillaklasse.

Mit diesem System kann ich die Verwaltung von Zoo-Tieren simulieren und 
meine Kenntnisse in der OOP vertiefen.


"""

from tiger import Tiger
from gorilla import Gorilla

def main():
    # Tiger-Instanz erstellen
    tiger = Tiger("Shera", 0, 5)
    tiger.eat()
    tiger.sleep()
    tiger.grow(3)
    tiger.roar()

    # Gorilla-Instanz erstellen
    gorilla = Gorilla("Koko", 1, 10)
    gorilla.eat()
    gorilla.sleep()
    gorilla.grow(2)
    gorilla.klettern()

if __name__ == "__main__":
    main()
