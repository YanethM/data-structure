import tkinter as tk
import pygame
# Inicializar el modulo de pygame
pygame.init()

# Crear dimensiones del display
window_width = 700
window_height = 600
display_game = pygame.display.set_mode((window_width, window_height))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 151)

# Variable que permitira mantener el display visible
display_game.fill(WHITE)
