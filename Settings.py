import pygame
pygame.init()
ASDFADSFGAS = pygame.display.set_mode((800, 600))
LENGTH = 10
WIDTH = 10
NUM_BOMBS = 20
CELL_SIZE = 50
CELL_COLOR = (255,255,255)
BACKGROUND_COLOR = (0,0,0)
BORDER_THICKNESS = 1
FONT = pygame.font.SysFont('Arial', 25)
TEXT_COLOR = (0,0,0)
SCREEN_WIDTH = CELL_SIZE * WIDTH
SCREEN_HEIGHT = CELL_SIZE * LENGTH
flag = pygame.image.load('/Users/sanjay/Downloads/Minesweeper flag.webp').convert()
flag = pygame.transform.scale(flag, (CELL_SIZE,CELL_SIZE))