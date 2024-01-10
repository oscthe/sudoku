import pygame
from board import Board


# Initialize Pygame
pygame.init()

if __name__ == "__main__":
    sudoku = Board()
    sudoku.run()
