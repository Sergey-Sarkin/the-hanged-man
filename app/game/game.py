from .storage import Storage
from .logic import Logic
from .ui import UI
import utils

def game_loop() -> None:
    """Game loop"""
    
    utils.clear_cmd()

    word_dict = Storage.load_word()
    
    word = word_dict["word"]
    description = word_dict["description"]

    logic = Logic(word, description)
    states = logic.create_base_states()

    while True:
        while not states["is_over"]:
            UI.display(states)
            letter = UI.read_letter()

            utils.clear_cmd()
            Logic.update_states(states, letter)

        is_win = UI.check_win(states)

        utils.clear_cmd()

        return