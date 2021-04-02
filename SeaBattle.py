print("Let's play in Battleship!")
print("Row is horizontal way 1-5")
print("COL is vertical way 1-5")
print("Good Luck")

from random import randint

board = []

for i in range (6):
    board.append(["o"] * 6)

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
for turn in range(6):
    print("Turn", turn + 1)

print(ship_col)
print(ship_row)


guess_row = int(input("ROOWW!!: "))
guess_col = int(input("COOOL: "))


if guess_row == ship_row and guess_col == ship_col:
    print("You win little Scammer!!")
else:
    if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
        print("Is not your spoot!!")
    elif (board[guess_row][guess_col] == "X"):
        print("Ohh hit one")
    else:
        print(" EEE You killed my battleship BITTCH")
        board[guess_row][guess_col] = "X"
        print("Turn:", turn +1 )
    print_board(board)
    if turn == 3:
        print("Game Over")