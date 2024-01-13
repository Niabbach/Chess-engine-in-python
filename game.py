#!pip install pygame
import pygame
import os

# Loading chess board and piece images
board = pygame.image.load(os.path.join("img", "board.png"))

b_bishop = pygame.image.load(os.path.join("img", "black-bishop.png"))
b_king = pygame.image.load(os.path.join("img", "black-king.png"))
b_knight = pygame.image.load(os.path.join("img", "black-knight.png"))
b_pawn = pygame.image.load(os.path.join("img", "black-pawn.png"))
b_queen = pygame.image.load(os.path.join("img", "black-queen.png"))
b_rook = pygame.image.load(os.path.join("img", "black-rook.png"))

w_bishop = pygame.image.load(os.path.join("img", "white-bishop.png"))
w_king = pygame.image.load(os.path.join("img", "white-king.png"))
w_knight = pygame.image.load(os.path.join("img", "white-knight.png"))
w_pawn = pygame.image.load(os.path.join("img", "white-pawn.png"))
w_queen = pygame.image.load(os.path.join("img", "white-queen.png"))
w_rook = pygame.image.load(os.path.join("img", "white-rook.png"))

# Storing images in lists and scaling them up
b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

B = [pygame.transform.scale2x(img) for img in b]
W = [pygame.transform.scale2x(img) for img in w]

# Function to redraw the game window
def redraw_gamewindow():
    global win
    win.blit(board, (0, 0))
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
            if event.type == pygame.MOUSEMOTION:
                pass  # Placeholder for mouse motion handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass  # Placeholder for mouse button down handling

# Setting up the game window
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Game")

main()
