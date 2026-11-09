from readchar import readkey

RUSSIAN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def display(states: dict) -> None:
    """Display game"""

    print(f"Подсказка: {states['description']}")
    print(f"Слово: {' '.join(states['display_word'])}")
    print(f"Попытки: {states['attempts']}")

def read_letter() -> str:
    """Read letter"""

    print(f"Введите букву: ", end='', flush=True)

    while True:
        letter = readkey().lower().strip()

        if letter in RUSSIAN_ALPHABET:
            break

    print(letter)
    return letter

def check_win(states: dict) -> None:
    """Cheke win"""
    
    if states["is_win"]:
        print("Победа!")
    else:
        print("Поражение!")

    input("Нажмите Enter, чтобы продолжить!")