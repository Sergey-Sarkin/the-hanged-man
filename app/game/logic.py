def create_base_states(word: str, description: str) -> dict[str, any]:
    """Create base game states"""

    return {
        "secret_word": word,
        "display_word": ["_"] * len(word),
        "description": description,
        "attempts": 5,
        "is_win": False,
        "is_over": False
    }

def update_states(states: dict[str, any], letter: str) -> None:
    """Update game staes"""
    
    if states["is_over"]:
        return
    
    is_mistake = True
    for index, letter_secret in enumerate(states["secret_word"]):
        if letter == letter_secret:
            states["display_word"][index] = letter
            is_mistake = False

    states["attempts"] -= 1 if is_mistake else 0

    if "_" not in states["display_word"]:
        states["is_win"] = True
        states["is_over"] = True

    if states["attempts"] <= 0:
        states["is_over"] = True