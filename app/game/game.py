from .storage import Storage
from .logic import Logic
from . import ui
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
            ui.display(states)
            letter = ui.read_letter()

            utils.clear_cmd()
            Logic.update_states(states, letter)

        is_win = ui.check_win(states)

        utils.clear_cmd()

        return