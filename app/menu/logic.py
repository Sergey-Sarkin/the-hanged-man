from readchar import key, readkey as read

def create_base_states() -> dict[str: any]:
    """Create base menu states"""

    return {
        "point": 0,
        "is_enter": False
    }

def get_point(menu_list: list[str], states: dict[str: any]) -> None:
    """Return point menu"""
    
    pressed_key = read()

    if pressed_key == key.ENTER:
        states['is_enter'] = True
    elif pressed_key == key.UP:
        if states['point'] == 0:
            states['point'] = len(menu_list) - 1
        else:
            states['point'] -= 1
    elif pressed_key == key.DOWN:
        if states['point'] == len(menu_list) - 1:
            states['point'] = 0
        else:
            states['point'] += 1