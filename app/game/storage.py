from pathlib import Path
from random import choice
from json import load, dumps

def load_word() -> dict[str, str]:
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

if __name__ == "__main__":
    word = load_word()
    json_string = dumps(word, indent=4, ensure_ascii=False)

    print(json_string)