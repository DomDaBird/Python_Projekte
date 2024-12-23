"""

@author: Dominik Vogel

api()


"""

import requests

# Basis-URL der PokeAPI
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def fetch_data(name):
    """
    Ruft die Daten eines Pokémon aus der PokeAPI ab.

    Args:
        name (str): Name des Pokémon.

    Returns:
        dict: JSON-Daten des Pokémon, falls die Anfrage erfolgreich ist.
        None: Falls das Pokémon nicht gefunden wird oder ein Fehler auftritt.
    """
    try:
        response = requests.get(f"{BASE_URL}{name.lower()}")
        response.raise_for_status()  # HTTP-Fehler auslösen
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Daten: {e}")
        return None

