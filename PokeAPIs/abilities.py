def extract_abilities(data):
    """
    Extrahiert die Fähigkeiten eines Pokémon aus den API-Daten.

    Args:
        data (dict): JSON-Daten des Pokémon.

    Returns:
        list: Liste der Fähigkeiten als Strings.
        None: Falls keine Fähigkeiten gefunden werden.
    """
    if 'abilities' in data:
        return [ability['ability']['name'].capitalize() for ability in data['abilities']]
    return None
