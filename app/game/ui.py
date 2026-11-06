from readchar import readkey

from logic import create_base_states

def display(states: dict) -> None:
    print(f"Подсказка: {states['description']}")
    print(f"Слово: {' '.join(states['display_word'])}")
    print(f"Попытки: {states['attempts']}")

if __name__ == "__main__":
    states = create_base_states()
    display(states)