from game import game
from menu import menu
import utils

def main():
    """Main function"""
    
    utils.clear_cmd()
    while True:
        match menu():
            case 0:
                game()
            case 1:
                return

if __name__ == "__main__":
    main()