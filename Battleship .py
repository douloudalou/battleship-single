from random import randint

board = []
ship_row = 0
ship_col = 0

for x in range(5):
    board.append(['O'] * 5)

def print_board(board):
    for row in board:
        print(('').join(row))

def Enemy_ship(board):
    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board) - 1)
    print(ship_row)
    print(ship_col)

def game(board):
    turn = 1
    print_board(board)
    Enemy_ship(board)

    while turn <= 5:
        print('Turn ' + str(turn)) 
        guess_row = int(input('Guess Row: '))
        guess_col = int(input('Guess Col: '))

        if guess_row == ship_row and guess_col == ship_col:
            print('Congrats!!! You sunk my ship!!!')
            break
        elif guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
            print('BRUH Thats not even on the board')
        elif board[guess_row][guess_col] == 'X':
            print('You already guessed that before')
        else:
            print('MISSED!!! HAHA!')
            board[guess_row][guess_col] = 'X'
        if turn == 5:
            print('!!!GAME OVER!!!')
            break
        print_board(board)
        turn+=1
        
game(board)


