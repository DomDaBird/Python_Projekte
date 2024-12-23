

"""

@author: Dominik Vogel


Projekt: Inputvalidierung

In diesem Projekt setze ich die gelernten Inhalte der Woche praktisch um, indem ich 
ein einfaches Interface erstelle, das die Eingaben der Benutzer überprüft und auf 
Gültigkeit prüft (Inputvalidierung). 

### Ziele:
1. Ich implementiere die Überprüfung der Nutzereingaben, um sicherzustellen, dass 
   nur gültige Daten akzeptiert werden.
2. Ich nutze Debug- und Infonachrichten, um die Funktionalität der Anwendung zu protokollieren.
3. Ich stelle sicher, dass unsachgemäße Eingaben (versehentlich oder absichtlich) 
   erkannt und behandelt werden, um Sicherheitslücken zu vermeiden.

### Struktur meines Programms:
- **Hauptfunktionen:**
  - `main()`: Diese Funktion steuert die gesamte Benutzerinteraktion, einschließlich der Eingabe von 
    Emailadresse und Alter.
  - `check_email(input_email)`: Validiert, ob die eingegebene Emailadresse gültig ist.
  - `check_age(input_age)`: Prüft, ob das eingegebene Alter innerhalb eines zulässigen Bereichs liegt.

- **Eingabeoptionen:**
  - `?`: Gibt die Docstrings der verfügbaren Funktionen mit dem Attribut `__doc__` aus.
  - `w`: Ermöglicht die Eingabe von Emailadresse und Alter. Bei fehlerhaften Eingaben werde ich den 
    Nutzer um neue Werte bitten.
  - `q`: Beendet das Programm.

- **Ablauf:**
  Mein Programm läuft in einer `while`-Schleife, die Benutzerinteraktionen verarbeitet. Die Schleife wird erst beendet, 
  wenn der Benutzer `q` eingibt.

### Anforderungen:
- **Docstrings:** Ich füge ausführliche Docstrings zu den Funktionen `check_email` und `check_age` hinzu.
- **Logging:** Ich nutze `logging` und verschiedene Logging-Stufen (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`), um 
  wichtige Ereignisse im Programmablauf zu dokumentieren.
- **Assertions:** 
  - Ich überprüfe, ob die Eingaben `?`, `q` oder `w` korrekt sind, und gebe bei einem Fehler eine entsprechende 
    Meldung aus.
  - Ich stelle sicher, dass die Emailadresse mindestens 5 Zeichen lang ist und sowohl ein "@" als auch einen Punkt enthält.
  - Das Alter muss zwischen 10 und 99 Jahren liegen. Falls dies nicht der Fall ist, wird ein Fehler erkannt und behandelt.

### Bonusaufgabe:
Zusätzlich entwickle ich eine Funktion, die ein vom Benutzer eingegebenes Passwort auf Stärke überprüft. Diese Funktion stellt sicher, dass das Passwort:
- eine Mindestlänge hat,
- Großbuchstaben enthält,
- mindestens eine Zahl und ein Sonderzeichen beinhaltet.

### Beispiel:
Hier ist eine Vorschau, wie die Benutzereingaben und die Ausgaben meines Programms aussehen könnten:

Drücke '?' um Hilfe zu bekommen.  
Drücke 'q' um die App zu verlassen.  
Drücke 'w' um weiterzumachen.  

> test  
2023-10-04 16:08:56,205 - ERROR - Bitte gib einen korrekten Input an!  

> ?  
check_email:  
    Die Funktion prüft, ob die eingegebene Emailadresse gültig ist.  

check_age:  
    Die Funktion prüft, ob die eingegebene Zahl ein valides Alter darstellt.  

> w  
Wie lautet deine Email?  
> fake-mail.com  
2023-10-04 16:09:47,156 - ERROR - Bitte gib eine korrekte Email an!  

> w  
Wie lautet deine Email?  
> name@mail.com  

Wie alt bist du?  
> abc  
2023-10-04 16:10:24,095 - ERROR - Bitte gib ein korrektes Alter an!  

> q  
2023-10-04 16:10:39,969 - DEBUG - Die Schleife wurde beendet.  


"""


import logging

# Logging konfigurieren
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_email(input_email: str):

    """
    Überprüft, ob eingegebene Emailadresse gültig ist.
    
    Eine gültige Emailadresse muss mindestens 5 Zeichen lang sein und 
    sowohl ein "@" als auch einen Punkt enthalten.
    
    Parameter:
    input_email (str): Die zu überprüfende Emailadresse.
    
    Returns:
    bool: True, wenn Emailadresse gültig ist, sonst False.
    """

    logging.info("Funktion 'check_email' wurde aufgerufen.")
    assert len(input_email) >= 5, "Emailadresse muss mindestens 5 Zeichen lang sein."
    assert "@" in input_email and "." in input_email, "Emailadresse muss '@' und '.' enthalten."
    return True

def check_age(input_age: str):

    """
    Überprüft, ob eingegebenes Alter gültig ist.
    
    Ein gültiges Alter muss eine Zahl zwischen 10 und 99 sein.
    
    Parameters:
    input_age (str): Das zu überprüfende Alter als String.
    
    Returns:
    int: Das Alter als Integer, wenn es gültig ist.
    """

    logging.info("Funktion 'check_age' wurde aufgerufen.")
    try:
        age = int(input_age)
    except ValueError:
        raise AssertionError("Das Alter muss eine Zahl sein.")
    
    assert 10 <= age <= 99, "Das Alter muss zwischen 10 und 99 Jahren liegen."
    return age

def main():

    """
    Steuert Programmablauf und ruft Validierungsfunktionen auf.
    """

    while True:
        user_input = input("Drücke '?' für Hilfe, 'w' für Eingabe, 'q' für Beenden: ").strip().lower()
        logging.debug(f"Eingabe des Nutzers: {user_input}")
        
        try:
            assert user_input in ['?', 'w', 'q'], "Ungültige Eingabe. Bitte '?' für Hilfe, 'w' für Eingabe, 'q' für Beenden eingeben."
        except AssertionError as e:
            logging.error(e)
            continue

        if user_input == '?':
            print(check_email.__doc__)
            print(check_age.__doc__)
        elif user_input == 'w':
            while True:
                email = input("Wie lautet deine Email? ")
                logging.debug(f"Eingegebene Email ist {email}.")
                try:
                    if check_email(email):
                        break
                except AssertionError as e:
                    logging.error(e)
                    print("Bitte gib eine korrekte Email an!")

            while True:
                age = input("Wie alt bist du? ")
                logging.debug(f"Eingegebenes Alter ist {age}.")
                try:
                    if check_age(age):
                        break
                except AssertionError as e:
                    logging.error(e)
                    print("Bitte gib ein korrektes Alter an!")
        
        elif user_input == 'q':
            logging.debug("Die Schleife wurde beendet.")
            break

def check_password_strength(password: str):

    """
    Überprüft Stärke eines Passworts anhand von Mindestanforderungen.
    
    Ein starkes Passwort muss enthalten:
    - Mindestens 8 Zeichen
    - Mindestens einen Großbuchstaben
    - Mindestens eine Zahl
    - Mindestens ein Sonderzeichen
    
    Parameters:
    password (str): Das zu überprüfende Passwort.
    
    Returns:
    bool: True, wenn das Passwort stark ist, sonst False.
    """
    
    logging.info("Funktion 'check_password_strength' wurde aufgerufen.")
    
    if len(password) < 8:
        logging.warning("Passwort muss mindestens 8 Zeichen lang sein.")
        return False
    if not any(char.isupper() for char in password):
        logging.warning("Passwort muss mindestens einen Großbuchstaben enthalten.")
        return False
    if not any(char.isdigit() for char in password):
        logging.warning("Passwort muss mindestens eine Zahl enthalten.")
        return False
    if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/~" for char in password):
        logging.warning("Passwort muss mindestens ein Sonderzeichen enthalten.")
        return False
    
    return True

if __name__ == "__main__":
    main()
