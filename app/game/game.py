from utils import Utils
from .storage import Storage
from .logic import Logic
from .ui import UI

class Game:
    @staticmethod
    def _loop(states: dict[str, str | int | bool | list[str]]) -> None:
        """Game loop"""

        while not states["is_over"]:
            UI.display(states)
            letter = UI.read_letter()
                
            Utils.clear_cmd()
            Logic.update_states(states, letter)

    @classmethod
    def _game_loop(cls, states: dict[str, str | int | bool | list[str]]) -> None:
        """Game game loop"""

        cls._loop(states) 
        UI.check_win(states)
        Utils.clear_cmd()

    @classmethod
    def game(cls) -> None:
        """Game game"""
            
        Utils.clear_cmd()
        
        word_dict = Storage.load_word()
            
        word = word_dict["word"]
        description = word_dict["description"]
        
        logic = Logic(word, description)
        states = logic.create_base_states()
        
        cls._game_loop(states)