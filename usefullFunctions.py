from colors import brown, white, properWhite, black, yellow
import chessBoardClass
import pygame
pygame.init()

squareSize = 100
markedButton = None
destinationButton = None
pieces = ['whitePawn', 'blackPawn', 'whiteRook', 'blackRook', 'whiteKnight', 'blackKnight', 'whiteBishop', 'blackBishop', 
          'whiteKing', 'blackKing', 'whiteQueen', 'blackQueen']

def setUptheBoard(chessBoard: chessBoardClass.chessBoard, screen, boardPosition: list, listOfSquares: list, dictOfSquares: dict):
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Chess')
    for row in range(chessBoard.width):
        for column in range(chessBoard.height):
            sqr = pygame.Rect(row*squareSize, column*squareSize, squareSize, squareSize)
            if row % 2 == 0:
                if column % 2 != 0:
                    pygame.draw.rect(screen, brown, sqr)
                else:
                    pygame.draw.rect(screen, white, sqr)
            else:
                if column % 2 != 0:
                    pygame.draw.rect(screen, white, sqr)
                else:
                    pygame.draw.rect(screen, brown, sqr)
            listOfSquares.append(sqr)

    for column in range(len(boardPosition)):
        for row in range(len(boardPosition[column])):
            for square in listOfSquares:
                if square.centerx == squareSize/2+column*squareSize and square.centery == squareSize/2+row*squareSize and boardPosition[column][row] != None:
                    img = pygame.image.load(f'C:\\VSCODE\\projekt pygame\\chess\\img\\{boardPosition[column][row]}.png')
                    img = pygame.transform.smoothscale(img, (squareSize, squareSize))
                    screen.blit(img, (row*squareSize, column*squareSize))

                    try:
                        dictOfSquares[boardPosition[column][row]].append(square)
                    except:
                        dictOfSquares[boardPosition[column][row]] = [square]

def findTheSquare(mousePosition, listOfButtons):
    for button in listOfButtons:
        if button.collidepoint(mousePosition):
            return button

def checkIfTheMoveIsPossible(chessBoard, StartButton, FinishButton):
    row = int(StartButton.x/squareSize)
    column = int(StartButton.y/squareSize)
    possibleSquares = []
    if chessBoard.boardModel[column][row] == None:
        return False
    if 'Bishop' in chessBoard.boardModel[column][row]:
        pass
    elif 'Rook' in chessBoard.boardModel[column][row]:
        pass
    elif 'King' in chessBoard.boardModel[column][row]:
        pass
    elif 'Pawn' in chessBoard.boardModel[column][row]:
        if chessBoard.boardModel[column][row] != None:
            if chessBoard.boardModel[column][row][0:5] == 'black':
                try:
                    if chessBoard.boardModel[column+1][row] == None:
                        possibleSquares.append(pygame.Rect(row*squareSize, (column+1)*squareSize, squareSize, squareSize))
                    if column == 1 and chessBoard.boardModel[column+2][row] == None:
                        possibleSquares.append(pygame.Rect(row*squareSize, (column+2)*squareSize, squareSize, squareSize))
                    if chessBoard.boardModel[column+1][row+1] != None:
                        possibleSquares.append(pygame.Rect((row+1)*squareSize, (column+1)*squareSize, squareSize, squareSize))
                    if chessBoard.boardModel[column+1][row-1] != None:
                        possibleSquares.append(pygame.Rect((row-1)*squareSize, (column+1)*squareSize, squareSize, squareSize))
                except:
                    pass
            elif chessBoard.boardModel[column][row][0:5] == 'white':
                pass
            print(possibleSquares)
    elif 'Queen' in chessBoard.boardModel[column][row]:
        pass
    elif 'Knight' in chessBoard.boardModel[column][row]:
        pass

    if FinishButton not in possibleSquares:
        return False

    return True