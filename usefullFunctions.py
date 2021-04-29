from colors import brown, white, properWhite, black
import chessBoardClass
import pygame
pygame.init()

def setUptheBoard(chessBoard: chessBoardClass.chessBoard, screen):
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Chess')
    for row in range(chessBoard.width):
        