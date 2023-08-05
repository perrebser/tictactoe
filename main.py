import random
import pygame
import numpy as np

pygame.init()

# Colors
BG = (230, 230, 230)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Window and board
WIDTH = 300
HEIGHT = 300
SQUARE_SIZE = WIDTH // 3
BOARD_ROWS = 3
BOARD_COLUMNS = 3

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

board = np.zeros((BOARD_ROWS, BOARD_COLUMNS), dtype=int)

players = [1, 2]
player = random.choice(players)
clicked = False  # Variable for detecting mouse click
pos = []  # Stores mouse position
game_over = False
font = pygame.font.SysFont(None, 40)
winner = None


def dibujar_tablero():
    window.fill(BG)
    for fila in range(3):
        for column in range(3):
            x = column * SQUARE_SIZE
            y = fila * SQUARE_SIZE
            pygame.draw.rect(window, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE), 2)


def draw_markers():
    for fila in range(3):
        for column in range(3):
            if board[fila][column] == 1:
                pygame.draw.circle(window, BLUE, (column * 100 + 50, fila * 100 + 50), 38, 6)
            elif board[fila][column] == 2:
                pygame.draw.line(window, RED, (column * 100 + 15, fila * 100 + 15),
                                 (column * 100 + 85, fila * 100 + 85), 6)
                pygame.draw.line(window, RED, (column * 100 + 15, fila * 100 + 85),
                                 (column * 100 + 85, fila * 100 + 15), 6)


def show_winner():
    global winner
    winner_text = "Player " + str(winner) + " wins!"
    win_img = font.render(winner_text, True, BLUE)
    pygame.draw.rect(window, WHITE, (WIDTH // 2 - 100, HEIGHT // 2, 200, 50))
    pygame.draw.rect(window, RED, (WIDTH // 2 - 100, HEIGHT // 2, 200, 50))
    window.blit(win_img, (WIDTH // 2 - 100 + 10, HEIGHT // 2 + 10))


def check_winner():
    global winner
    global game_over
    # Check rows and columns
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player) or \
                (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            game_over = True
            winner = player

    # Check diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
            (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        winner = player
        game_over = True


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                pos = pygame.mouse.get_pos()
                x_mouse = pos[0] // SQUARE_SIZE
                y_mouse = pos[1] // SQUARE_SIZE
                if board[y_mouse][x_mouse] == 0:  # Empty cell
                    board[y_mouse][x_mouse] = player
                    check_winner()
                    player = 3 - player

    dibujar_tablero()
    draw_markers()
    if game_over:
        show_winner()
    pygame.display.update()
