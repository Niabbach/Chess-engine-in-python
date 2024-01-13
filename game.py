#!pip install pygame
import pygame
import os
from piece import Bishop
# Loading chess board
board = pygame.transform.scale(pygame.image.load(os.path.join("img", "board.png")),(550,550))
rect = (50,50,455,455)

# Function to redraw the game window
def redraw_gamewindow():
    global win
    win.blit(board, (0, 0))
    b = Bishop(1,1,"w")
    b.draw(win)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(10)
        redraw_gamewindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Set run to False to exit the loop and close the window
                quit()
                pygame.quit()
            
            if event.type == pygame.MOUSEMOTION:
                pass  # Placeholder for mouse motion handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass  # Placeholder for mouse button down handling

# Setting up the game window
width = 550
height = 550
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Game")

main()
