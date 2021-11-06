import pygame
from pprint import pprint
from math import ceil
from pygame import color
from pygame.constants import MOUSEBUTTONDOWN
import chessBoardClass
from usefullFunctions import setUptheBoard, findTheSquare, checkIfTheMoveIsPossible, ifItIsAMate
pygame.init()
import sys

pieces = ['whitePawn', 'blackPawn', 'whiteRook', 'blackRook', 'whiteKnight', 'blackKnight', 'whiteBishop', 'blackBishop', 
          'whiteKing', 'blackKing', 'whiteQueen', 'blackQueen']

squareSize = 100         
listOfSquares = []
listOfMenuButtons = []
dictOfSquares = dict()
chessBoard = chessBoardClass.chessBoard()
screen = pygame.display.set_mode((400, 400))
secondClick = False
clickedButton = None
mouseSignature = None
destinationButton = None
submode = 'white'
submodes = {'white':'black', 'black':'white'}
lastMove = {'piece':None, 'column':None, 'row':None}
copyOfLastMove = {'piece':None, 'column':None, 'row':None}

mode = 'preparingToPickUpAPiece'
clock = pygame.time.Clock()

setUptheBoard(chessBoard, screen, chessBoard.boardModel, listOfSquares, dictOfSquares)
while True:
    if mode == 'menu':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    if mode == 'preparingToPickUpAPiece':
        
        if ifItIsAMate(screen, chessBoard, submode, lastMove):
            print('mat')
            mode = 'mate'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                clickedButton = findTheSquare(mouse_position, listOfSquares)
                mouseSignature = chessBoard.boardModel[int(clickedButton.y/100)][int(clickedButton.x/100)]
                mode = 'pickedUpAPiece'
    if mode == 'pickedUpAPiece':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = event.pos
                destinationButton = findTheSquare(mouse_position, listOfSquares)
                copyOfLastMove = lastMove
                if checkIfTheMoveIsPossible(screen, chessBoard, clickedButton, destinationButton, lastMove) and mouseSignature[0:5] == submode:
                    #autopromotion to queen - change that in the future
                    if (destinationButton.y/100 == chessBoard.height-1 or destinationButton.y/100 == 0) and 'Pawn' in chessBoard.boardModel[int(clickedButton.y/100)][int(clickedButton.x/100)]:
                        chessBoard.boardModel[int(destinationButton.y/100)][int(destinationButton.x/100)] = mouseSignature[0:5] + 'Queen'
                    else:
                        chessBoard.boardModel[int(destinationButton.y/100)][int(destinationButton.x/100)] = mouseSignature
                    chessBoard.boardModel[int(clickedButton.y/100)][int(clickedButton.x/100)] = None
                    setUptheBoard(chessBoard, screen, chessBoard.boardModel, listOfSquares, dictOfSquares)
                    submode = submodes[submode]
                else:
                    lastMove = copyOfLastMove
                mode = 'preparingToPickUpAPiece'
    if mode == 'mate':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
    pygame.display.update()
    clock.tick(60)