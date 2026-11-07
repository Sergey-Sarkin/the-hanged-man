from readchar import readkey, key

def get_point() -> int:
    points = [1, 2]

    index = 0
    while True:
        pressed_key = readkey()

        if pressed_key == key.UP:
            if index == 0:
                index = len(points) - 1
            else:
                index -= 1

        elif pressed_key == key.DOWN:
            if index == len(points) - 1:
                index = 0
            else:
                index += 1

        elif pressed_key == key.ENTER:
            return points[index]

if __name__ == "__main__":
    point = get_point()
    print(point)