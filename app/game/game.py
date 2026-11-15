import utils
from .storage import Storage
from .logic import Logic
from .ui import UI

class Game:
    @staticmethod
    def _loop(states: dict[str, str | int | bool | list[str]]) -> None:
        while not states["is_over"]:
            UI.display(states)
            letter = UI.read_letter()
                
            utils.clear_cmd()
            Logic.update_states(states, letter)

    @classmethod
    def _game_loop(cls, states: dict[str, str | int | bool | list[str]]) -> None:
        cls._loop(states) 
        UI.check_win(states)
        utils.clear_cmd()

    @classmethod
    def game(cls) -> None:
        """Game loop"""
            
        utils.clear_cmd()
        
        word_dict = Storage.load_word()
            
        word = word_dict["word"]
        description = word_dict["description"]
        
        logic = Logic(word, description)
        states = logic.create_base_states()
        
        cls._game_loop(states)