def display(point: int) -> None:
    print("Играть <" if point == 1 else "Играть")
    print("Выход <" if point == 2 else "Выход")

if __name__ == "__main__":
    display(1)