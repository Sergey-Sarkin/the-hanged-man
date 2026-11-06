from json import dumps

def create_base_states(word: str, description: str) -> dict[str, any]:
    return {
        "secret_word": word,
        "display_word": ["_"] * len(word),
        "description": description,
        "attempts": 5,
        "is_win": False,
        "is_over": False
    }

def update_states(states: dict[str, any], letter: str) -> None:
    if states["is_over"]:
        return
    
    found = True
    for index, letter_secret in enumerate(states["secret_word"]):
        if letter == letter_secret:
            states["display_word"][index] = letter
            found = False

    states["attempts"] -= 1 if found else 0

    if "_" not in states["display_word"]:
        states["is_win"] = True
        states["is_over"] = True

    if states["attempts"] <= 0:
        states["is_over"] = True