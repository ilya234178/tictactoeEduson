from colorama import Fore, Back, Style, init
init(autoreset=True)
def draw_board(board):

    for i in range(3):
        colored_row = []
        for j in range(3):
            cell = board[i][j]
            if cell == "X":
                colored_row.append(Fore.RED + cell + Fore.RESET)
            elif cell == "O":
                colored_row.append(Fore.BLUE + cell + Fore.RESET)
            else:
                colored_row.append(Back.YELLOW + cell + Back.RESET)
        print(" | ".join(colored_row))
        if i < 2:
            print("---------")

def ask_and_make_move(player, board):
    x, y = ask_move(player, board)

    make_move(player, board, x, y)
    

def ask_move(player, board):
    while True:
        try:
            x, y = input(f"{player}, enter x and y coordinates (e.g. 0 0): ").strip().split()
            x, y = int(x), int(y)
        except ValueError:
            print("Please enter two valid numbers")
            continue
            
        if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "): 
            return (x, y)
        else:
            print("Клетка занята. Введите координаты еще раз.")
              

def make_move(player, board, x, y):
    if board[x][y] != " ":
        print("Клетка занята")
        return False
    board[x][y] = player
    return True

def check_win(player, board):
    for i in range(3):
        if board[i] == [player, player, player]:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def tic_tac_toe():
    while True:
        board = [[" " for i in range(3)] for j in range(3)]
        player = "X"

        while True:
            draw_board(board)
            ask_and_make_move(player, board)

            if check_win(player, board):
                print(f"{player} you wins!")
                draw_board(board)
                break

            if check_draw(board):
                print("Ничья!")
                draw_board(board)
                break
            

            player = "O" if player == "X" else "X"

        restart = input("Хотите сыграть еще раз? (y/n) ")    
        if restart.lower() != "y":
            break

tic_tac_toe()