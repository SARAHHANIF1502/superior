class Calculator:
    def __init__(self):
        self.Operations={
            "+":self.add,
            "-":self.substract,
            "*":self.multiply,
            "/":self.division
        }
    def add(self,a,b):
        return a+b
    def substract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def division(self,a,b):
        if b!=0:
            return a/b
        else:
            raise ValueError("Cannot divide by zero!")
    def calculate(self,operator,a,b):
        if operator in self.Operations:
            return self.Operations[operator](a, b)
        else:
            raise ValueError(f"Operation {operator} not supported.")
    def add_operation(self, operator, function):
        self.Operations[operator] = function
    def list_operations(self):
        return list(self.operations.keys())
cal1 = Calculator()
print(cal1.calculate('+',18, 2)) 
print(cal1.calculate('-',18, 2))  
print(cal1.calculate('*',18 ,2))  
print(cal1.calculate('/',18,2))  
dynamic tictactoe game using minmax algorithuim
import sys
import pygame
import numpy as np
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

FONT = pygame.font.Font(None, 80)


def create_board(size):
    return np.zeros((size, size))

def draw_lines(board_size):
    for row in range(1, board_size):
        pygame.draw.line(screen, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (row * SQUARE_SIZE, 0), (row * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures(board, board_size):
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, BLUE, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, BLUE, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def mark_square(row, col, player, board):
    board[row][col] = player

def available_square(row, col, board):
    return board[row][col] == 0

def check_win(player, board, board_size):
    for row in range(board_size):
        if np.all(board[row, :] == player):
            return True

    for col in range(board_size):
        if np.all(board[:, col] == player):
            return True

    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False

def is_board_full(board):
    return np.all(board != 0)

def draw_winner(player):
    win_text = FONT.render(f"Player {player} wins!", True, BLACK)
    screen.blit(win_text, (WIDTH // 4, HEIGHT // 3))

def draw_tie():
    tie_text = FONT.render("It's a Tie!", True, BLACK)
    screen.blit(tie_text, (WIDTH // 3, HEIGHT // 3))


def minimax(board, depth, is_maximizing, board_size):
    if check_win(2, board, board_size): 
        return 1
    if check_win(1, board, board_size): 
        return -1
    if is_board_full(board): 
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(board_size):
            for col in range(board_size):
                if available_square(row, col, board):
                    board[row][col] = 2
                    score = minimax(board, depth + 1, False, board_size)
                    board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(board_size):
            for col in range(board_size):
                if available_square(row, col, board):
                    board[row][col] = 1
                    score = minimax(board, depth + 1, True, board_size)
                    board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score

def ai_move(board, board_size):
    best_score = -float('inf')
    move = None
    for row in range(board_size):
        for col in range(board_size):
            if available_square(row, col, board):
                board[row][col] = 2
                score = minimax(board, 0, False, board_size)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def main():
    global BOARD_ROWS, BOARD_COLS, SQUARE_SIZE
    board_size = int(input("Choose board size (3, 4, or 5): "))

    if board_size not in [3, 4, 5]:
        print("Invalid board size. Defaulting to 3x3.")
        board_size = 3

    BOARD_ROWS, BOARD_COLS = board_size, board_size
    SQUARE_SIZE = WIDTH // board_size

    board = create_board(board_size)
    screen.fill(WHITE)
    draw_lines(board_size)
    player = 1 
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if available_square(clicked_row, clicked_col, board):
                    mark_square(clicked_row, clicked_col, player, board)
                    draw_figures(board, board_size)

                    if check_win(player, board, board_size):
                        draw_winner(player)
                        game_over = True

                    if is_board_full(board) and not game_over:
                        draw_tie()
                        game_over = True

                    player = 2 if player == 1 else 1

        if player == 2 and not game_over: 
            ai_row, ai_col = ai_move(board, board_size)
            mark_square(ai_row, ai_col, 2, board)
            draw_figures(board, board_size)

            if check_win(2, board, board_size):
                draw_winner(2)
                game_over = True

            if is_board_full(board) and not game_over:
                draw_tie()
                game_over = True

            player = 1  

        pygame.display.update()

if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Dynamic Tic-Tac-Toe')
    main()
