n = 4
board = [[0] * n for _ in range(n)]

def safe(row, col):

    # column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(row):
    if row == n:
        return True

    for col in range(n):
        if safe(row, col):
            board[row][col] = 1
            if solve(row + 1):
                return True
            board[row][col] = 0

    return False


solve(0)

for row in board:
    print(row)