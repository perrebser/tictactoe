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
TAMANO_CASILLA = WIDTH // 3
BOARD_ROWS = 3
BOARD_COLUMNS = 3

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

board = np.zeros((BOARD_ROWS, BOARD_COLUMNS),dtype=int)

players = [1, 2]
player = random.choice(players)
clicked = False  # Variable for detecting mouse click
pos = []  # Stores mouse position


def dibujar_tablero():
    for fila in range(3):
        for column in range(3):
            x = column * TAMANO_CASILLA
            y = fila * TAMANO_CASILLA
            pygame.draw.rect(window, WHITE, (x, y, TAMANO_CASILLA, TAMANO_CASILLA), 2)

def draw_markers():
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            x_mouse = pos[0]
            y_mouse = pos[1]
            if board[x_mouse // 100][y_mouse // 100] == 0: #Empty cell
                board[x_mouse // 100][y_mouse // 100] = player

    window.fill(BG)
    dibujar_tablero()
    pygame.display.update()
