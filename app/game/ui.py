from readchar import readkey

RUSSIAN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def display(states: dict) -> None:
    print(f"Подсказка: {states['description']}")
    print(f"Слово: {' '.join(states['display_word'])}")
    print(f"Попытки: {states['attempts']}")

def read_letter() -> str:
    print(f"Введите букву: ", end='', flush=True)

    while True:
        letter = readkey().lower().strip()

        if letter in RUSSIAN_ALPHABET:
            break
        
    print(letter)
    return letter