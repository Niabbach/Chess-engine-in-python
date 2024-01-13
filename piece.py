import pygame
import os

# Loading piece images
b_bishop = pygame.transform.scale(pygame.image.load(os.path.join("img", "black-bishop.png")),(30,30))
b_king = pygame.transform.scale(pygame.image.load(os.path.join("img", "black-king.png")),(30,30))
b_knight = pygame.transform.scale(pygame.image.load(os.path.join("img", "black-knight.png")),(30,30))
b_pawn = pygame.transform.scale(pygame.image.load(os.path.join("img", "black-pawn.png")),(30,30))
b_queen = pygame.transform.scale(pygame.image.load(os.path.join("img", "black-queen.png")),(30,30))
b_rook = pygame.transform.scale(pygame.image.load(os.path.join("img", "black-rook.png")),(30,30))

w_bishop = pygame.transform.scale(pygame.image.load(os.path.join("img", "white-bishop.png")),(30,30))
w_king = pygame.transform.scale(pygame.image.load(os.path.join("img", "white-king.png")),(30,30))
w_knight = pygame.transform.scale(pygame.image.load(os.path.join("img", "white-knight.png")),(30,30))
w_pawn = pygame.transform.scale(pygame.image.load(os.path.join("img", "white-pawn.png")),(30,30))
w_queen = pygame.transform.scale(pygame.image.load(os.path.join("img", "white-queen.png")),(30,30))
w_rook = pygame.transform.scale(pygame.image.load(os.path.join("img", "white-rook.png")),(30,30))

# Storing images in lists and scaling them up
b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

B = [pygame.transform.scale2x(img) for img in b]
W = [pygame.transform.scale2x(img) for img in w]


class Piece:
    img = -1
    rect = (50,50,455,455)
    startX = rect[0]
    startY = rect[1]
    def __init__(self, row, col,color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False


    def move(self):
        pass
    
    def isSelected(self):
        return self.selected
    
    def draw(self, win):
        if self.color == "w":
            drawThis = W[self.img]
        else:
            drawThis = B[self.img]
        
        x = self.startX + (self.col * self.rect[2]/8)
        y = self.startY + (self.row * self.rect[2]/8)

        win.blit(drawThis, (x, y))


class Bishop(Piece):
    img = 0

class King(Piece):
     img = 1

class Knight(Piece):
     img = 2

class Pawn(Piece):
     img = 3

class Queen(Piece):
     img = 4

class Rook(Piece):
     img = 5