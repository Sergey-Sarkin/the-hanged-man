from . import storage, logic, ui
import utils

def game_loop() -> None:
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

        if states["is_win"]:
            print("Победа")
            return
        else:
            print("Поражение")
            return