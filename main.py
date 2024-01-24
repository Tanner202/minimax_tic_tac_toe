def check_for_win(board, symbol):
    if diagonal_check(board, symbol) or check_horizontal(board, symbol) or check_vertical(board, symbol):
        return True
    return False

def diagonal_check(board, symbol):
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    else:
        return False

def check_horizontal(board, symbol):
    if board[0][0] == board[0][1] == board[0][2] == symbol:
        return True
    elif board[1][0] == board[1][1] == board[1][2] == symbol:
        return True
    elif board[2][0] == board[2][1] == board[2][2] == symbol:
        return True
    else:
        return False

def check_vertical(board, symbol):
    if board[0][0] == board[1][0] == board[2][0] == symbol:
        return True
    elif board[0][1] == board[1][1] == board[2][1] == symbol:
        return True
    elif board[0][2] == board[1][2] == board[2][2] == symbol:
        return True
    else:
        return False

def get_available_spaces(board):
    available_spaces = []
    for row_index in range(len(board)): 
        for col_index in range(len(board[row_index])):
            if board[row_index][col_index] == "":
                available_spaces.append((row_index, col_index))
    return available_spaces

def minimax(board, is_max_player, depth):
    available_spaces = get_available_spaces(board)
    if check_for_win(board, "X"):
        return 10 - depth
    elif check_for_win(board, "O"):
        return -10 - depth
    elif len(available_spaces) == 0:
        return 0

    moves = []

    if is_max_player:
        for available_space in available_spaces:
            row = available_space[0]
            col = available_space[1]
            new_board = [x[:] for x in board]
            new_board[row][col] = "X"
            score = minimax(new_board, False, depth + 1)
            moves.append((score, new_board))
        best_move = (-9999, None)
        for move in moves:
            if move[0] > best_move[0]:
                best_move = move

        if depth == 0:
            return best_move
        else:
            return best_move[0]
    else:
        for available_space in available_spaces:
            row = available_space[0]
            col = available_space[1]
            new_board = [x[:] for x in board]
            new_board[row][col] = "O"
            score = minimax(new_board, True, depth + 1)
            moves.append((score, new_board))
        best_move = (9999999, None)
        for move in moves:
            if move[0] < best_move[0]:
                best_move = move
        if depth == 0:
            return best_move
        else:
            return best_move[0]

class Board():
    def __init__(self):
        self.board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

    def set_position(self, move, row, col):
        self.board[row][col] = move

    def __str__(self):
        print_statement = ""
        for row_index in range(len(self.board)):
            for col_index in range(len(self.board[row_index])):
                if col_index != 2:
                    print_statement += str(self.board[row_index][col_index]) + "|"
                else:
                    print_statement += str(self.board[row_index][col_index])
            if row_index != 2:
                print_statement += "\n-|-|-\n"
        return print_statement

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]


playing = True

while playing:
    coords = input("Where do you want to play? (x, y)\n")
    x, y = coords.split(",")
    board[int(y)][int(x)] = "O"
    board = minimax(board, True, 0)[1]
    for row in board:
        print(row)

    if check_for_win(board, "X"):
        print("X wins!")
        playing = False
    if check_for_win(board, "O"):
        print("O wins!")
        playing = False