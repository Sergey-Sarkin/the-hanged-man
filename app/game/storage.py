from json import load
from pathlib import Path
from random import choice
import sys

class Storage:
    _words: list[dict[str, str]] | None = None
    _DEFAULT_WORD: dict[str, str] = {
        'word': 'кит', 
        'description': 'Самое крупное в мире морское млекопитающее, дышащее воздухом.'
    }

    @staticmethod
    def _get_path_dir() -> Path:
        """Get base directory path."""

        if getattr(sys, "frozen", False):
            return Path(sys._MEIPASS)
        return Path(__file__).resolve().parent.parent.parent

    @classmethod
    def load_word(cls) -> dict[str, str]:
        """Load word and description."""

        if cls._words is None:
            path_dir = cls._get_path_dir()
            path_file = path_dir / "data" / "words.json"

            if not path_file.exists():
                cls._words = []
            else:
                with path_file.open("r", encoding="utf-8") as file:
                    cls._words = load(file)

        if not cls._words:
            return cls._DEFAULT_WORD.copy()

        return choice(cls._words).copy()