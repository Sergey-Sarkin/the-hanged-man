from . import logic, storage, ui
import utils

def game_loop() -> None:
    """Game loop"""
    
    utils.clear_cmd()

    word_dict = storage.load_word()
    
    word = word_dict["word"]
    description = word_dict["description"]

    states = logic.create_base_states(word, description)
    while True:
        while not states["is_over"]:
            ui.display(states)
            letter = ui.read_letter()

            utils.clear_cmd()
            logic.update_states(states, letter)

        is_win = ui.check_win(states)

        utils.clear_cmd()

        return