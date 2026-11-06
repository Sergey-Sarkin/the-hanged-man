from readchar import readkey

from logic import create_base_states

def display(states: dict) -> None:
    print(f"Подсказка: {states['description']}")
    print(f"Слово: {' '.join(states['display_word'])}")
    print(f"Попытки: {states['attempts']}")

def read_letter() -> str:
    print(f"Введите букву: ", end='', flush=True)
    letter = readkey().lower().strip()
    print(letter)
    return letter

if __name__ == "__main__":
    states = create_base_states()
    display(states)
    read_letter()