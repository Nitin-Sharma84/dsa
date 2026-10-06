board=[
    ['.','.','.'],
    ['.','.','.'],
    ['.','.','.']
    ]

def winner(player):
    if ((player == board[0][0] and player == board[0][1] and player == board[0][2]) or 
       (player == board[1][0] and player == board[1][1] and player == board[1][2]) or 
       (player == board[2][0] and player == board[2][1] and player == board[2][2]) or 
       (player == board[0][0] and player == board[1][0] and player == board[2][0]) or 
       (player == board[0][1] and player == board[1][1] and player == board[2][1]) or 
       (player == board[0][2] and player == board[1][2] and player == board[2][2]) or 
       (player == board[0][0] and player == board[1][1] and player == board[2][2]) or 
       (player == board[0][2] and player == board[1][1] and player == board[2][0])):

        return True

    return False
def show_board(board):
    for b in board:
        print(b)

moves=0
player='x'
while True:
    moves+=1
    if moves==10:
        print("Game Tie")
        break
    show_board(board)
    print(f"Player {player}")
    in1=int(input("Enter input 1: "))
    in2=int(input("Enter input 2: "))
    board[in1][in2]=player
    if winner(player):
        show_board(board)
        print(f'Player {player} is winner')
        break
    if player=='x':
        player='o'
    else:
        player='x'
