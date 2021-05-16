import pygame
from pprint import pprint
from math import ceil
from pygame.constants import MOUSEBUTTONDOWN
import chessBoardClass
from usefullFunctions import setUptheBoard
pygame.init()

pieces = ['whitePawn', 'blackPawn', 'whiteRook', 'blackRook', 'whiteKnight', 'blackKnight', 'whiteBishop', 'blackBishop', 
          'whiteKing', 'blackKing', 'whiteQueen', 'blackQueen']
          
listOfSquares = []
chessBoard = chessBoardClass.chessBoard()
screen = pygame.display.set_mode((400, 400))

running = True

setUptheBoard(chessBoard, screen, chessBoard.boardModel, listOfSquares)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_possition = pygame.mouse.get_pos()
            for button in listOfSquares:
                pass
        
    pygame.display.update()