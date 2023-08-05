import random
import pygame
import numpy as np
from tkinter import messagebox

pygame.init()

# Colors
BG = (230, 230, 230)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Window and board
WIDTH = 300
HEIGHT = 300
TAMANO_CASILLA = WIDTH // 3
BOARD_ROWS = 3
BOARD_COLUMNS = 3

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

board = np.zeros((BOARD_ROWS, BOARD_COLUMNS), dtype=int)

players = [1, 2]
player = random.choice(players)
clicked = False  # Variable for detecting mouse click
pos = []  # Stores mouse position
run = True
game_over = False


def dibujar_tablero():
    for fila in range(3):
        for column in range(3):
            x = column * TAMANO_CASILLA
            y = fila * TAMANO_CASILLA
            pygame.draw.rect(window, WHITE, (x, y, TAMANO_CASILLA, TAMANO_CASILLA), 2)


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


def check_winner(player):
    global game_over
    # Check rows and columns
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player) or \
                (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            game_over = True
            return True

    # Check diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
            (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        game_over = True
        return True

    return False


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                pos = pygame.mouse.get_pos()
                x_mouse = pos[0] // TAMANO_CASILLA
                y_mouse = pos[1] // TAMANO_CASILLA
                if board[y_mouse][x_mouse] == 0:  # Empty cell
                    board[y_mouse][x_mouse] = player
                    player = abs(player - 3)
                if check_winner(player):
                    print(f"Player {player} wins!")


    window.fill(BG)
    dibujar_tablero()
    draw_markers()
    pygame.display.update()
