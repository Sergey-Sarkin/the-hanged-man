from .logic import Logic
from .ui import UI
from utils import Utils

class Menu:
    @staticmethod
    def menu_loop() -> int:
        """Menu loop"""
        
        states = Logic.create_base_states()
        menu_list = ["Играть", "Выйти"]
        
        while not states['is_enter']:
            UI.display_menu(menu_list, states['point'])
            Logic.get_point(menu_list, states)
            Utils.clear_cmd()
        
        return states['point']

# def menu_loop() -> int:
#     """Menu loop"""

#     states = Logic.create_base_states()
#     menu_list = ["Играть", "Выйти"]

#     while not states['is_enter']:
#         UI.display_menu(menu_list, states['point'])
#         Logic.get_point(menu_list, states)
#         Utils.clear_cmd()

#     return states['point']