def extract_sprite(data):
    """
    Extrahiert den Front-Sprite-Link aus den Pokémon-Daten.

    Args:
        data (dict): JSON-Daten des Pokémon.

    Returns:
        str: URL des Front-Sprites, falls vorhanden.
        None: Falls kein Sprite gefunden wird.
    """
    if 'sprites' in data and 'front_default' in data['sprites']:
        return data['sprites']['front_default']
    return None
