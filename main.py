import pygame
import numpy as np


pygame.init()

# Colors
BG = (230, 230, 230)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Window and board
WIDTH = 400
HEIGHT = 400
TAMANO_CASILLA = WIDTH // 3
BOARD_ROWS = 3
BOARD_COLUMNS = 3

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))


def dibujar_tablero():
    for fila in range(3):
        for column in range(3):
            x = column * TAMANO_CASILLA
            y = fila * TAMANO_CASILLA
            pygame.draw.rect(window, WHITE, (x, y, TAMANO_CASILLA, TAMANO_CASILLA), 2)


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    window.fill(BG)
    dibujar_tablero()
    pygame.display.update()
