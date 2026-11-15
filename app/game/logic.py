class Logic:
    def __init__(self, word: str, description: str) -> None:
        self._word = word
        self._description = description

    def create_base_states(self) -> dict[str, str | int | bool | list[str]]:
        """Create base game states"""

        return {
            "secret_word": self._word,
            "display_word": ["_"] * len(self._word),
            "description": self._description,
            "attempts": 5,
            "is_win": False,
            "is_over": False
        }

    @staticmethod
    def _update_display_word(states: dict[str, str | int | bool | list[str]], letter: str) -> bool:
        """Update display_word"""

        is_mistake = True
        for index, letter_secret in enumerate(states["secret_word"]):
            if letter == letter_secret:
                states["display_word"][index] = letter
                is_mistake = False

        return is_mistake

    @staticmethod
    def _update_attempts(states: dict[str, str | int | bool | list[str]], is_mistake: bool) -> None:
        """Update attempts"""

        states["attempts"] -= 1 if is_mistake else 0

    @staticmethod
    def _update_over_win(states: dict[str, str | int | bool | list[str]]) -> None:
        """Update is_over and is_win"""

        if "_" not in states["display_word"]:
            states["is_win"] = True
            states["is_over"] = True
                
        if states["attempts"] <= 0:
            states["is_over"] = True

    @classmethod
    def update_states(cls, states: dict[str, str | int | bool | list[str]], letter: str) -> None:
        """Update game states"""

        if states["is_over"]:
            return

        is_mistake = cls._update_display_word(states, letter)
        cls._update_attempts(states, is_mistake)
        cls._update_over_win(states)