from game import Game
from menu import menu
from utils import Utils

def main():
    """Main function"""
    
    Utils.clear_cmd()
    while True:
        match menu():
            case 0:
                Game.game()
            case 1:
                return

if __name__ == "__main__":
    main()