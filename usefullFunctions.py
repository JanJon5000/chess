from colors import brown, white, properWhite, black
import chessBoardClass
import pygame
pygame.init()

def setUptheBoard(chessBoard: chessBoardClass.chessBoard, screen):
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Chess')
    for row in range(chessBoard.width):
        for column in range(chessBoard.height):
            sqr = pygame.Rect(row*50, column*50, 50, 50)
            if row % 2 == 0:
                pygame.draw.rect(screen, brown, sqr)
            else:
                pygame.draw.rect(screen, white, sqr)