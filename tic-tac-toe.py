import random
print("Hanish S Adhi - 1BM24CS109")
board = [" "] * 9
WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)]


def show():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("---+---+---")
    print()


def winner():
    for a, b, c in WINS:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


def empty():
    return [i for i, cell in enumerate(board) if cell == " "]


def player_move():
    while True:
        try:
            pos = int(input("Your move (1-9): ")) - 1
            if pos in empty():
                board[pos] = "X"
                return
        except ValueError:
            pass
        print("Invalid move. Try again.")


def computer_move():
    pos = random.choice(empty())
    board[pos] = "O"
    print(f"Computer plays {pos + 1}")


show()
print("Positions: 1 2 3 / 4 5 6 / 7 8 9")

while True:
    player_move()
    show()
    if winner() == "X":
        print("You win!")
        break
    if not empty():
        print("It's a draw.")
        break

    computer_move()
    show()
    if winner() == "O":
        print("Computer wins!")
        break
    if not empty():
        print("It's a draw.")
        break