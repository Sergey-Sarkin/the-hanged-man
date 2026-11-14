import sys
from pathlib import Path
from random import choice
from json import load

class Storage:
    @staticmethod
    def load_word() -> dict[str, str]:
        """Load word and description"""

        path_dir = None

        if getattr(sys, 'frozen', False):
            path_dir = Path(sys._MEIPASS)
        else:
            path_dir = Path(__file__).resolve().parent.parent.parent

        path_words = path_dir / "data" / "words.json"
        words = []

        if not path_words.exists():
            raise FileNotFoundError("the path does not exist")

        with path_words.open("r", encoding="utf-8") as file:
            words = load(file)

        if not words:
            return {
                'word': 'кит', 
                'description': 'Самое крупное в мире морское млекопитающее, дышащее воздухом.'
            }

        return choice(words)