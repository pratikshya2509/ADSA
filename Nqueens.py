def is_safe(row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def nqueen(row):
    if row == n:
        print_board()
        return

    for col in range(n):
        if is_safe(row, col):
            board[row] = col
            nqueen(row + 1)
            board[row] = -1


def print_board():
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


n = int(input("Enter number of queens: "))

board = [-1] * n

nqueen(0)
