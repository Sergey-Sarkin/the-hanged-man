from . import logic, ui
from utils import Utils

def menu_loop() -> int:
    """Menu loop"""

    states = logic.create_base_states()
    menu_list = ["Играть", "Выйти"]

    while not states['is_enter']:
        ui.display_menu(menu_list, states['point'])
        logic.get_point(menu_list, states)
        Utils.clear_cmd()

    return states['point']