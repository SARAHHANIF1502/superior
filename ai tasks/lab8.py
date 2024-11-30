import random

board = [' ' for _ in range(9)]

def place_mark(mark, position):
    board[position] = mark

def is_position_empty(position):
    return board[position] == ' '

def display_board():
    print()
    print('   |   |')
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[6]} | {board[7]} | {board[8]}')
    print('   |   |')
    print()

def is_board_full():
    return board.count(' ') == 0

def is_winner(current_board, mark):
    return (
        (current_board[0] == mark and current_board[1] == mark and current_board[2] == mark) or
        (current_board[3] == mark and current_board[4] == mark and current_board[5] == mark) or
        (current_board[6] == mark and current_board[7] == mark and current_board[8] == mark) or
        (current_board[0] == mark and current_board[3] == mark and current_board[6] == mark) or
        (current_board[1] == mark and current_board[4] == mark and current_board[7] == mark) or
        (current_board[2] == mark and current_board[5] == mark and current_board[8] == mark) or
        (current_board[0] == mark and current_board[4] == mark and current_board[8] == mark) or
        (current_board[2] == mark and current_board[4] == mark and current_board[6] == mark)
    )

def computer_turn():
    best_score = -float('inf')
    best_move = 0
    for i in range(9):
        if is_position_empty(i):
            place_mark('O', i)
            score = minimax(board, 0, False)
            place_mark(' ', i)
            if score > best_score:
                best_score = score
                best_move = i
    place_mark('O', best_move)

def minimax(current_board, depth, is_maximizing):
    if is_winner(current_board, 'O'):
        return 10
    if is_winner(current_board, 'X'):
        return -10
    if is_board_full():
        return 0
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if is_position_empty(i):
                place_mark('O', i)
                score = minimax(current_board, depth + 1, False)
                place_mark(' ', i)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if is_position_empty(i):
                place_mark('X', i)
                score = minimax(current_board, depth + 1, True)
                place_mark(' ', i)
                best_score = min(score, best_score)
        return best_score

def main():
    print("Tic-Tac-Toe Game")
    display_board()
    while not is_board_full():
        player_move = input("Enter your move (1-9): ")
        if is_position_empty(int(player_move) - 1):
            place_mark('X', int(player_move) - 1)
            display_board()
            if is_winner(board, 'X'):
                print("You win!")
                break
            if is_board_full():
                print("It's a tie!")
                break
            computer_turn()
            display_board()
            if is_winner(board, 'O'):
                print("Computer wins!")
                break
        else:
            print("Invalid move, try again.")

if __name__ == "__main__":
    main()
