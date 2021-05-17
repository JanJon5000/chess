import pygame
from pprint import pprint
from math import ceil
from pygame.constants import MOUSEBUTTONDOWN
import chessBoardClass
from usefullFunctions import setUptheBoard, findTheSquare
pygame.init()

pieces = ['whitePawn', 'blackPawn', 'whiteRook', 'blackRook', 'whiteKnight', 'blackKnight', 'whiteBishop', 'blackBishop', 
          'whiteKing', 'blackKing', 'whiteQueen', 'blackQueen']

squareSize = 100         
listOfSquares = []
dictOfSquares = dict()
chessBoard = chessBoardClass.chessBoard()
screen = pygame.display.set_mode((400, 400))
secondClick = False
running = True

mode = 'preparingToPickUpAPiece'

setUptheBoard(chessBoard, screen, chessBoard.boardModel, listOfSquares, dictOfSquares)
while running:
    if mode == 'preparingToPickUpAPiece':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                clickedButton = findTheSquare(mouse_position, listOfSquares)
                mouseSignature = chessBoard.boardModel[int(clickedButton.y/100)][int(clickedButton.x/100)]
                chessBoard.boardModel[int(clickedButton.y/100)][int(clickedButton.x/100)] = None                
                mode = 'pickedUpAPiece'
    if mode == 'pickedUpAPiece':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = event.pos
                img = pygame.image.load(f'C:\\VSCODE\\projekt pygame\\chess\\img\\{mouseSignature}.png')
                img = pygame.transform.smoothscale(img, (squareSize, squareSize))
                setUptheBoard(chessBoard, screen, chessBoard.boardModel, listOfSquares, dictOfSquares)
                screen.blit(img, (mouse_position[0]-squareSize/2, mouse_position[1]-squareSize/2))
                mode = 'preparingToPickUpAPiece'
    pygame.display.update()