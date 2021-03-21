print(" " * 9, "Epic Battle")
def greet():
    print("-------------------------------------------------")
    print(" ------------------ Hello------------------------")
    print(" pick: x y ")
    print(" x - line  ")
    print(" y - column ")

greet()

field = [[" "] * 3 for i in range(3) ]
def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

show()


def ask():
    while True:
        cords = input("         Your turn: ").split()

        if len(cords) != 2:
            print(" enter 2 coordinates! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" enter numbers! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" out of range! ")
            continue

        if field[x][y] != " ":
            print(" cell is busy! ")
            continue

        return x, y

ask()

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Win X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Win 0!!!")
            return True
    return False

field = [
    [" ", "X", " "],
    [" ", "X", " "],
    [" ", "X", " "]
]

check_win()

greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Turn X")
    else:
        print(" Turn 0")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Drawn Game  ")
        break







