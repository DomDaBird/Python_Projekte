#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Dominik Vogel


## Projektbeschreibung

In diesem Projekt erstelle ich ein Programm zur Cäsar-Verschlüsselung, 
einem der ältesten bekannten Verschlüsselungsverfahren. Dabei verschiebe 
ich die Buchstaben eines Textes basierend auf einer festgelegten Verschiebungszahl im Alphabet.

Der Ablauf meines Programms sieht folgendermaßen aus:
1. Ich fordere den Benutzer auf, einen Text einzugeben, der nur aus Kleinbuchstaben besteht.
2. Danach frage ich eine Verschiebungszahl ab, die angibt, um wie viele Stellen jeder Buchstabe verschoben wird.
3. Anschließend verschlüssele ich den eingegebenen Text basierend auf der Cäsar-Verschlüsselung 
   und gebe das Ergebnis in der Konsole aus.
4. Optional ermögliche ich es, den verschlüsselten Text wieder in den ursprünglichen Text zu entschlüsseln.

### Tipps für die Umsetzung:
- Ich nutze `ord()` und `chr()`, um Buchstaben in ASCII-Werte und zurück zu konvertieren.
- Mit dem Modulo-Operator `%` stelle ich sicher, dass die Verschiebung zyklisch bleibt, 
  sodass nach 'z' wieder 'a' beginnt.
- Die ASCII-Werte für Kleinbuchstaben reichen von 97 ('a') bis 122 ('z').

### Beispiel:
Eingabe:
    Text: hallo
    Verschiebung: 3

Ausgabe:
    Verschlüsselter Text: kdoor

Optional, Rückentschlüsselung:
    Verschlüsselter Text: kdoor
    Ursprünglicher Text: hallo


    
===============================================
CAESAR
===============================================
Gib den zu verschlüsselnden Text ein:
divide et impera
===============================================
Wähle eine Verschiebung: 3
===============================================
glylgh hw lpshud
===============================================
Noch einmal? (j/n) 

"""

def caesar_encrypt(text, shift):
    
    """
    
    Verschlüsselt einen Text mit der angegebenen Verschiebung (Cäsar-Verschlüsselung).

    Der zu verschlüsselnde Text (nur Kleinbuchstaben)
    Die Anzahl der Positionen, um die jeder Buchstabe verschoben wird
    Der verschlüsselte Text
    
    """
    
    encrypted_text = ""

    for char in text:
        if char.isalpha(): # Berechnet neuen verschlüsselten Charakter
            new_char = chr(((ord(char) - 97 + shift) % 26) + 97)
            encrypted_text += new_char
        else:
            encrypted_text += char  # Leerzeichen oder andere Zeichen unverändert lassen

    return encrypted_text

def caesar_decrypt(text, shift):
    
    """
    
    Entschlüsselt einen Text mit der angegebenen Verschiebung (Cäsar-Verschlüsselung).
    Der zu entschlüsselnde Text (nur Kleinbuchstaben)
    Die Anzahl der Positionen, um die jeder Buchstabe verschoben wurde
    Der entschlüsselte Text
    
    """
    
    decrypted_text = ""

    for char in text:
        if char.isalpha(): # Berechnet den neuen entschlüsselten Charakter
            new_char = chr(((ord(char) - 97 - shift) % 26) + 97)
            decrypted_text += new_char
        else:
            decrypted_text += char  # Leerzeichen oder andere Zeichen unverändert lassen

    return decrypted_text

def main():
    """
    
    Hauptprogramm für die Cäsar-Verschlüsselung.
    
    """
    
    while True:
        print("===============================================")
        print()
        print("===============     CAESAR      ===============")
        print()
        print("===============================================")
        print()
        text = input("Gib den zu verschlüsselnden Text ein (nur Kleinbuchstaben): ").lower()
        print("Verschlüsselung 2: a ==> c")
        print("Verschlüsselung 3: a ==> d")
        print("Verschlüsselung 10: a ==> k")
        print("usw...")
        shift = int(input("Wähle eine Verschiebung (NUR ZAHL): "))
        
        encrypted_text = caesar_encrypt(text, shift)  # Verschlüsseln des Textes
        print("===============================================")
        print()
        print("Verschlüsselter Text:", encrypted_text)
        print()
        print("===============================================")

        decrypt_option = input("Möchtest du den Text entschlüsseln? (j/n): ").lower()
        if decrypt_option == 'j':
            decrypted_text = caesar_decrypt(encrypted_text, shift)
            print("Entschlüsselter Text:", decrypted_text)

        again = input("Noch einmal? (j/n): ").lower() # Möglichkeit, das Programm erneut zu starten
        if again != 'j':
            break

if __name__ == "__main__":
    main()
