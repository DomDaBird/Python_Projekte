"""

@author: Dominik Vogel

Pokedex!!!


"""


import streamlit as st
from api import fetch_data
from sprites import extract_sprite
from abilities import extract_abilities

# Titel und Beschreibung der Anwendung
st.title("Pokedex")
st.write("Willkommen beim Pokedex! Gib den Namen eines Pokémon ein, um Informationen zu erhalten.")

# Eingabefeld für den Pokémon-Namen
name = st.text_input("Gib den Namen eines Pokémon ein:")

if name:
    # Daten vom API abrufen
    data = fetch_data(name)

    if data:
        # Umrechnung in Standardmaßeinheiten
        height_meters = data['height'] / 10  # Dezimeter -> Meter
        weight_kg = data['weight'] / 10  # Hektogramm -> Kilogramm

        # Pokémon-Informationen anzeigen
        st.subheader(f"Informationen über {data['name'].capitalize()}")
        st.write(f"**Größe:** {height_meters:.2f} Meter")
        st.write(f"**Gewicht:** {weight_kg:.2f} Kilogramm")

        # Fähigkeiten anzeigen
        st.subheader("Fähigkeiten")
        abilities = extract_abilities(data)
        if abilities:
            st.write(", ".join(abilities))
        else:
            st.write("Keine Fähigkeiten verfügbar.")

        # Sprites anzeigen
        st.subheader("Sprites")
        sprite_url = extract_sprite(data)
        if sprite_url:
            st.image(sprite_url, caption=f"{data['name'].capitalize()} (Vorderansicht)")
        else:
            st.write("Kein Bild verfügbar.")

        # Option zum Schließen des Pokedex
        st.subheader("Pokedex schließen")
        close_pokedex = st.radio("Möchtest du deinen Pokedex schließen?", ("Nein", "Ja"))
        if close_pokedex == "Ja":
            st.write("Dein Pokedex wurde zurück in deinen Rucksack gelegt.")
            st.stop()
    else:
        st.error("Pokémon nicht gefunden. Bitte überprüfe den Namen.")
