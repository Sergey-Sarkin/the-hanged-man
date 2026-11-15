from readchar import readkey

class UI:
    _RUSSIAN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    @staticmethod
    def display(states: dict[str, str | int | bool | list[str]]) -> None:
        """Display game"""

        print(f"Подсказка: {states['description']}")
        print(f"Слово: {' '.join(states['display_word'])}")
        print(f"Попытки: {states['attempts']}")

    @classmethod 
    def read_letter(cls) -> str:
        """Read letter"""

        print("Введите букву: ", end="", flush=True)

        while True:
            letter = readkey().lower().strip()

            if len(letter) == 1 and letter in cls._RUSSIAN_ALPHABET:
                break 

        print(letter)
        return letter

    @staticmethod
    def check_win(states: dict[str, str | int | bool | list[str]]) -> None:
        """Check win"""
    
        if states["is_win"]:
            print("Победа!")
        else:
            print(f"Поражение! Загаданное слово '{states['secret_word']}'")

        input("Нажмите Enter, чтобы продолжить!")