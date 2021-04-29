import pygame
from pprint import pprint
import chessBoardClass
from usefullFunctions import setUptheBoard
pygame.init()

chessBoard = chessBoardClass.chessBoard()
pprint(chessBoard.boardModel)
screen = pygame.display.set_mode((400, 400))

running = True

setUptheBoard(chessBoard, screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()