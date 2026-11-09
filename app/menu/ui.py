def display_menu(menu_list: list[str], current_index: int) -> None:
    """Display menu"""

    for index, point in enumerate(menu_list):
        message = f"{point} <" if index == current_index else point
        print(message)