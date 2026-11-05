from json import dumps

from storage import load_word as load

def create_base_states() -> dict[str, any]:
    word_dict = load()

    word = word_dict["word"]
    description = word_dict["description"]

    return {
        "secret_word": word,
        "display_word": ["_"] * len(word),
        "description": description,
        "attempts": 5,
        "is_win": False,
        "is_over": False
    }

if __name__ == "__main__":
    states = create_base_states()
    states_json = dumps(states, indent=4, ensure_ascii=False)

    print(states_json)