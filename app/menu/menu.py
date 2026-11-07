from . import logic, ui
import utils
from game import game

def menu():
    while True:
        utils.clear_cmd()

        point = logic.get_point()
        ui.display(point)

        match point:
            case 1:
                game()
            case 2:
                break

if __name__ == "__main__":
    menu()