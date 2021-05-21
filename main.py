import pygame
from pprint import pprint
from math import ceil
from pygame.constants import MOUSEBUTTONDOWN
import chessBoardClass
from usefullFunctions import setUptheBoard, findTheSquare, checkIfTheMoveIsPossible
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
clickedButton = None
mouseSignature = None
destinationButton = None

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
                mode = 'pickedUpAPiece'
    if mode == 'pickedUpAPiece':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = event.pos
                destinationButton = findTheSquare(mouse_position, listOfSquares)
                if checkIfTheMoveIsPossible(chessBoard, clickedButton, destinationButton):
                    #autopromotion to queen - change that in the future
                    if (destinationButton.y/100 == chessBoard.height-1 or destinationButton.y/100 == 0) and 'Pawn' in chessBoard.boardModel[int(clickedButton.y/100)][int(clickedButton.x/100)]:
                        chessBoard.boardModel[int(destinationButton.y/100)][int(destinationButton.x/100)] = mouseSignature[0:5] + 'Queen'
                    else:
                        chessBoard.boardModel[int(destinationButton.y/100)][int(destinationButton.x/100)] = mouseSignature
                    chessBoard.boardModel[int(clickedButton.y/100)][int(clickedButton.x/100)] = None
                    setUptheBoard(chessBoard, screen, chessBoard.boardModel, listOfSquares, dictOfSquares)
                    
                
                mode = 'preparingToPickUpAPiece'
    pygame.display.update()