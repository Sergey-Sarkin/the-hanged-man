def clear_cmd() -> None:
    """The function clears the console on Windows"""

    print("\033[H\033[J", end="")