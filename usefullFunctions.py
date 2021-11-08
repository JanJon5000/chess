from pygame.constants import OPENGL
from colors import brown, white, properWhite, black, yellow, red, gray
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
    screen.fill(gray)
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
                    img = pygame.image.load(f'img\\{boardPosition[column][row]}.png')
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
def findTheKing(color, chessBoard):
    for row in chessBoard.boardModel:
        for column in row:
            if column == (color + 'King'):
                return pygame.Rect(row.index(column)*squareSize, chessBoard.boardModel.index(row)*squareSize, squareSize, squareSize)
    return -1, -1, -1
def pureIfItIsACheck(screen, chessBoard, color:str):
    dangers = []
    for row in chessBoard.boardModel:
        for piece in row:
            if piece == color + 'King':
                r = row.index(piece)
                c = chessBoard.boardModel.index(row)
    for index in range(4):
        for ammount in [ _ for _ in range(1, 8)]:
            moves = {  0:{'column':c+ammount, 'row':r+ammount},
                        1:{'column':c-ammount, 'row':r-ammount},
                        2:{'column':c-ammount, 'row':r+ammount},
                        3:{'column':c+ammount, 'row':r-ammount},
                        4:{'column':c, 'row':r+ammount},
                        5:{'column':c, 'row':r-ammount},
                        6:{'column':c+ammount, 'row':r},
                        7:{'column':c-ammount, 'row':r}       }
            try:
                column = moves[index]['column']
                row = moves[index]['row']
            except:
                pass
            try:
                square = chessBoard.boardModel[column][row]
            except:
                break
            try:
                if square == None:
                    continue
                elif color in square:
                    break
                elif not column < 0 and not row < 0:
                    dangers.append({'piece':square, 'column':column, 'row':row})
                    break
            except:
                pass
    moves = [(-2, (-1, 1)), (-1, (-2, 2)), (2, (-1, 1)), (1, (-2, 2))]
    for coordinates in moves:
        try:
            if 'Knight' in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][0]] and color not in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][0]] and c-coordinates[0] >= 0 and r-coordinates[1][0] >= 0:
                dangers.append({'piece':chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][0]], 'column':c-coordinates[0], 'row':r-coordinates[1][0]})
        except:
            pass
        try:
            if 'Knight' in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][1]] and color not in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][1]] and c-coordinates[0] >= 0 and r-coordinates[1][1] >= 0:
                dangers.append({'piece':chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][1]], 'column':c-coordinates[0], 'row':r-coordinates[1][1]})
        except:
            pass
    if dangers == []:
        return False
    else:
        return True

def dangers(screen, chessBoard, color:str):
    dangers = []
    for row in chessBoard.boardModel:
        for piece in row:
            if piece == color + 'King':
                r = row.index(piece)
                c = chessBoard.boardModel.index(row)
    for index in range(4):
        for ammount in [ _ for _ in range(1, 8)]:
            moves = {  0:{'column':c+ammount, 'row':r+ammount},
                        1:{'column':c-ammount, 'row':r-ammount},
                        2:{'column':c-ammount, 'row':r+ammount},
                        3:{'column':c+ammount, 'row':r-ammount},
                        4:{'column':c, 'row':r+ammount},
                        5:{'column':c, 'row':r-ammount},
                        6:{'column':c+ammount, 'row':r},
                        7:{'column':c-ammount, 'row':r}       }
            try:
                column = moves[index]['column']
                row = moves[index]['row']
            except:
                pass
            try:
                square = chessBoard.boardModel[column][row]
            except:
                break
            try:
                if square == None:
                    continue
                elif color in square:
                    break
                elif not column < 0 and not row < 0:
                    dangers.append({'piece':square, 'column':column, 'row':row})
                    break
            except:
                pass
    moves = [(-2, (-1, 1)), (-1, (-2, 2)), (2, (-1, 1)), (1, (-2, 2))]
    for coordinates in moves:
        try:
            if 'Knight' in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][0]] and color not in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][0]] and c-coordinates[0] >= 0 and r-coordinates[1][0] >= 0:
                dangers.append({'piece':chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][0]], 'column':c-coordinates[0], 'row':r-coordinates[1][0]})
        except:
            pass
        try:
            if 'Knight' in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][1]] and color not in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][1]] and c-coordinates[0] >= 0 and r-coordinates[1][1] >= 0:
                dangers.append({'piece':chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][1]], 'column':c-coordinates[0], 'row':r-coordinates[1][1]})
        except:
            pass
    return dangers
    
def ifItIsACheck(screen, chessBoard, color: str):
    actualMoves = []
    dangers = []
    r = 0
    c = 0
    for row in chessBoard.boardModel:
        for piece in row:
            if piece == color + 'King':
                r = row.index(piece)
                c = chessBoard.boardModel.index(row)
    for index in range(4):
        for ammount in [ _ for _ in range(1, 8)]:
            moves = {  0:{'column':c+ammount, 'row':r+ammount},
                        1:{'column':c-ammount, 'row':r-ammount},
                        2:{'column':c-ammount, 'row':r+ammount},
                        3:{'column':c+ammount, 'row':r-ammount},
                        4:{'column':c, 'row':r+ammount},
                        5:{'column':c, 'row':r-ammount},
                        6:{'column':c+ammount, 'row':r},
                        7:{'column':c-ammount, 'row':r}       }
            try:
                column = moves[index]['column']
                row = moves[index]['row']
            except:
                pass
            try:
                square = chessBoard.boardModel[column][row]
            except:
                break
            try:
                if square == None:
                    continue
                elif color in square:
                    break
                elif not column < 0 and not row < 0:
                    dangers.append({'piece':square, 'column':column, 'row':row})
                    break
            except:
                pass
    moves = [(-2, (-1, 1)), (-1, (-2, 2)), (2, (-1, 1)), (1, (-2, 2))]
    for coordinates in moves:
        try:
            if 'Knight' in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][0]] and color not in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][0]] and c-coordinates[0] >= 0 and r-coordinates[1][0] >= 0:
                dangers.append({'piece':chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][0]], 'column':c-coordinates[0], 'row':r-coordinates[1][0]})
        except:
            pass
        try:
            if 'Knight' in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][1]] and color not in chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][1]] and c-coordinates[0] >= 0 and r-coordinates[1][1] >= 0:
                dangers.append({'piece':chessBoard.boardModel[c-coordinates[0]][r-coordinates[1][1]], 'column':c-coordinates[0], 'row':r-coordinates[1][1]})
        except:
            pass
    if len(dangers) >= 1:
        return True
    elif len(dangers) < 1:
        return False

def checkIfTheMoveIsPossible(screen, chessBoard, StartButton, FinishButton, movedPiece):
    movedPieceSave = movedPiece['piece']
    row = int(StartButton.x/squareSize)
    column = int(StartButton.y/squareSize)
    possibleSquares = []
    color = None
    if chessBoard.boardModel[column][row] == None:
        return False
    if 'Bishop' in chessBoard.boardModel[column][row]:
        if chessBoard.boardModel[column][row][0:5] == 'black':
            color = 'black'
        elif chessBoard.boardModel[column][row][0:5] == 'white':
            color = 'white'
        
        movedPiece['piece'] = color + 'Bishop'
        for index in range(4):
            for ammount in [1, 2, 3, 4, 5, 6, 7, 8]:
                helpDictionary = {  0:{'column':column+ammount, 'row':row+ammount},
                                    1:{'column':column-ammount, 'row':row-ammount},
                                    2:{'column':column-ammount, 'row':row+ammount},
                                    3:{'column':column+ammount, 'row':row-ammount}    }
                try:
                    c = helpDictionary[index]['column']
                    r = helpDictionary[index]['row']
                except:
                    pass
                try:
                    square = chessBoard.boardModel[c][r]
                except:
                    break
                try:
                    if square == None:
                        possibleSquares.append(pygame.Rect(r*squareSize, c*squareSize, squareSize, squareSize))
                    elif color in chessBoard.boardModel[c][r]:
                        break
                    else:
                        possibleSquares.append(pygame.Rect(r*squareSize, c*squareSize, squareSize, squareSize))
                        break
                except:
                    pass
    elif 'Rook' in chessBoard.boardModel[column][row]:
        if chessBoard.boardModel[column][row][0:5] == 'black':
            color = 'black'
        elif chessBoard.boardModel[column][row][0:5] == 'white':
            color = 'white'

        movedPiece['piece'] = color + 'Rook'
        for index in range(4):
            for ammount in [1, 2, 3, 4, 5, 6, 7, 8]:
                helpDictionary = {  0:{'column':column+ammount, 'row':row},
                                    1:{'column':column-ammount, 'row':row},
                                    2:{'column':column, 'row':row+ammount},
                                    3:{'column':column, 'row':row-ammount}    }
                try:
                    c = helpDictionary[index]['column']
                    r = helpDictionary[index]['row']
                except:
                    pass
                try:
                    square = chessBoard.boardModel[c][r]
                except:
                    break
                try:
                    if square == None:
                        possibleSquares.append(pygame.Rect(r*squareSize, c*squareSize, squareSize, squareSize))
                    elif color in chessBoard.boardModel[c][r]:
                        break
                    else:
                        possibleSquares.append(pygame.Rect(r*squareSize, c*squareSize, squareSize, squareSize))
                        break
                except:
                    pass
    elif 'King' in chessBoard.boardModel[column][row]:
        if chessBoard.boardModel[column][row][0:5] == 'black':
            color = 'black'
        elif chessBoard.boardModel[column][row][0:5] == 'white':
            color = 'white'

        movedPiece['piece'] = color + 'King'
        for change1 in (1, -1):
            for change2 in (-1, 0, 1):
                try:
                    if chessBoard.boardModel[column-change1][row-change2] == None:
                        possibleSquares.append(pygame.Rect((row-change2)*squareSize, (column-change1)*squareSize, squareSize, squareSize))
                    elif color not in chessBoard.boardModel[column-change1][row-change2]:
                        possibleSquares.append(pygame.Rect((row-change2)*squareSize, (column-change1)*squareSize, squareSize, squareSize))
                except:
                    pass
                try:
                    if chessBoard.boardModel[column-change2][row-change1] == None:
                        possibleSquares.append(pygame.Rect((row-change1)*squareSize, (column-change2)*squareSize, squareSize, squareSize))
                    elif color not in chessBoard.boardModel[column-change2][row-change1]:
                        possibleSquares.append(pygame.Rect((row-change1)*squareSize, (column-change2)*squareSize, squareSize, squareSize))
                except:
                    pass
    elif 'Pawn' in chessBoard.boardModel[column][row]:
        if chessBoard.boardModel[column][row][0:5] == 'black':
            color = 'black'
        elif chessBoard.boardModel[column][row][0:5] == 'white':
            color = 'white'
        
        movedPiece['piece'] = color + 'Pawn'
        if chessBoard.boardModel[column][row] != None:
            if chessBoard.boardModel[column][row][0:5] == 'black':
                try:
                    if chessBoard.boardModel[column+1][row] == None:
                        possibleSquares.append(pygame.Rect(row*squareSize, (column+1)*squareSize, squareSize, squareSize))
                    if column == 1 and chessBoard.boardModel[column+2][row] == None:
                        possibleSquares.append(pygame.Rect(row*squareSize, (column+2)*squareSize, squareSize, squareSize))
                except:
                    pass
                try:
                    if chessBoard.boardModel[column+1][row+1] != None and 'black' not in chessBoard.boardModel[column+1][row+1]:
                        possibleSquares.append(pygame.Rect((row+1)*squareSize, (column+1)*squareSize, squareSize, squareSize))
                except:
                    pass
                try:
                    if chessBoard.boardModel[column+1][row-1] != None and 'black' not in chessBoard.boardModel[column+1][row-1] :
                        possibleSquares.append(pygame.Rect((row-1)*squareSize, (column+1)*squareSize, squareSize, squareSize))
                except:
                    pass
            elif chessBoard.boardModel[column][row][0:5] == 'white':
                try:
                    if chessBoard.boardModel[column-1][row] == None :
                        possibleSquares.append(pygame.Rect(row*squareSize, (column-1)*squareSize, squareSize, squareSize))
                    if column == chessBoard.height-2 and chessBoard.boardModel[column-2][row] == None:
                        possibleSquares.append(pygame.Rect(row*squareSize, (column-2)*squareSize, squareSize, squareSize))
                except:
                    pass
                try:
                    if chessBoard.boardModel[column-1][row-1] != None and 'white' not in chessBoard.boardModel[column-1][row-1] :
                        possibleSquares.append(pygame.Rect((row-1)*squareSize, (column-1)*squareSize, squareSize, squareSize))
                except:
                    pass
                try:
                    if chessBoard.boardModel[column-1][row+1] != None and 'white' not in chessBoard.boardModel[column-1][row+1] :
                        possibleSquares.append(pygame.Rect((row+1)*squareSize, (column-1)*squareSize, squareSize, squareSize))
                except:
                    pass
    elif 'Queen' in chessBoard.boardModel[column][row]:
        if chessBoard.boardModel[column][row][0:5] == 'black':
            color = 'black'
        elif chessBoard.boardModel[column][row][0:5] == 'white':
            color = 'white'
        
        movedPiece['piece'] = color + 'Queen'
        for index in range(8):
            for ammount in [1, 2, 3, 4, 5, 6, 7, 8]:
                helpDictionary = {  0:{'column':column+ammount, 'row':row+ammount},
                                    1:{'column':column-ammount, 'row':row-ammount},
                                    2:{'column':column-ammount, 'row':row+ammount},
                                    3:{'column':column+ammount, 'row':row-ammount},
                                    4:{'column':column, 'row':row+ammount},
                                    5:{'column':column, 'row':row-ammount},
                                    6:{'column':column+ammount, 'row':row},
                                    7:{'column':column-ammount, 'row':row}       }
                try:
                    c = helpDictionary[index]['column']
                    r = helpDictionary[index]['row']
                except:
                    pass
                try:
                    square = chessBoard.boardModel[c][r]
                except:
                    break
                try:
                    if square == None:
                        possibleSquares.append(pygame.Rect(r*squareSize, c*squareSize, squareSize, squareSize))
                    elif color in chessBoard.boardModel[c][r]:
                        break
                    else:
                        possibleSquares.append(pygame.Rect(r*squareSize, c*squareSize, squareSize, squareSize))
                        break
                except:
                    pass
    elif 'Knight' in chessBoard.boardModel[column][row]:
        if chessBoard.boardModel[column][row][0:5] == 'black':
            color = 'black'
        elif chessBoard.boardModel[column][row][0:5] == 'white':
            color = 'white'

        movedPiece['piece'] = color + 'Knight'
        possibleMoves = [ (-2, (-1, 1)), (-1, (-2, 2)), (2, (-1, 1)), (1, (-2, 2))]
        for coordinates in possibleMoves:
            try:
                if chessBoard.boardModel[column-coordinates[0]][row-coordinates[1][0]] == None:
                    possibleSquares.append(pygame.Rect((row-coordinates[1][0])*squareSize, (column-coordinates[0])*squareSize, squareSize, squareSize))
                elif color not in chessBoard.boardModel[column-coordinates[0]][row-coordinates[1][0]]:
                    possibleSquares.append(pygame.Rect((row-coordinates[1][0])*squareSize, (column-coordinates[0])*squareSize, squareSize, squareSize))
            except:
                pass
            try:
                if chessBoard.boardModel[column-coordinates[0]][row-coordinates[1][1]] == None:
                    possibleSquares.append(pygame.Rect((row-coordinates[1][1])*squareSize, (column-coordinates[0])*squareSize, squareSize, squareSize))
                elif color not in chessBoard.boardModel[column-coordinates[0]][row-coordinates[1][1]]:
                    possibleSquares.append(pygame.Rect((row-coordinates[1][1])*squareSize, (column-coordinates[0])*squareSize, squareSize, squareSize))
            except:
                pass
    if ifItIsACheck(screen, chessBoard, color):
        if FinishButton in possibleSquares:
            r2, c2 = int(FinishButton.x/squareSize), int(FinishButton.y/squareSize)
            chessBoard.boardModel[c2][r2] = chessBoard.boardModel[column][row]
            chessBoard.boardModel[column][row] = None
            if pureIfItIsACheck(screen, chessBoard, color):
                chessBoard.boardModel[column][row] = chessBoard.boardModel[c2][r2]
                chessBoard.boardModel[c2][r2] = None
                movedPiece['piece'] = movedPieceSave
            else:
                movedPiece['column'] = c2
                movedPiece['row'] = r2
                return True
    elif FinishButton in possibleSquares:
        movedPiece['column'] = int(FinishButton.y/squareSize)
        movedPiece['row'] = int(FinishButton.x/squareSize)
        return True
    movedPiece['piece'] = movedPieceSave
    return False

def areThereEspcapes(chessBoard, screen, color):
    surroundingSquares = [(-1, -1), (-1, 0), (1, -1), (0, -1), (0, 1), (-1, 1), (1, 0), (1, 1)]
    kingSquare = findTheKing(color, chessBoard)
    kingSquare = (int(kingSquare.y/squareSize), int(kingSquare.x/squareSize))
    for square in surroundingSquares:
            try:
                if color not in str(chessBoard.boardModel[kingSquare[0]+square[0]][kingSquare[1]+square[1]]):
                    if kingSquare[0]+square[0] >= 0 and kingSquare[1]+square[1] >= 0:
                        currentlyReviewedSquare = chessBoard.boardModel[kingSquare[0]+square[0]][kingSquare[1]+square[1]]
                        chessBoard.boardModel[kingSquare[0]][kingSquare[1]] = None
                        chessBoard.boardModel[kingSquare[0]+square[0]][kingSquare[1]+square[1]] = color + 'King'
                        if pureIfItIsACheck(screen, chessBoard, color):
                            chessBoard.boardModel[kingSquare[0]][kingSquare[1]] = color + 'King'
                            chessBoard.boardModel[kingSquare[0]+square[0]][kingSquare[1]+square[1]] = currentlyReviewedSquare
                        else:
                            chessBoard.boardModel[kingSquare[0]][kingSquare[1]] = color + 'King'
                            chessBoard.boardModel[kingSquare[0]+square[0]][kingSquare[1]+square[1]] = currentlyReviewedSquare
                            return False
            except:
                pass
    return True

def ifItIsAMate(screen, chessBoard, color, lastMove: dict):
    surroundingSquares = [(-1, -1), (-1, 0), (1, -1), (0, -1), (0, 1), (-1, 1), (1, 0), (1, 1)]
    kingSquare = findTheKing(color, chessBoard)
    kingSquare = (int(kingSquare.y/squareSize), int(kingSquare.x/squareSize))
    dangersList = dangers(screen, chessBoard, color)
    if len(dangersList) > 1:
        return areThereEspcapes(chessBoard, screen, color)
    else:
        truth = areThereEspcapes(chessBoard, screen, color)
        dangersList = dangersList[0]
        squaresToCover = []
        #linia bądź rząd - ten sam - wieża/królowa
        if dangersList['column'] == kingSquare[1]:
            for column in range(min(dangersList['column'], kingSquare[1]), max(dangersList['column'], kingSquare[1])):
                squaresToCover.append(pygame.Rect(column*squareSize, dangersList['row']*squareSize, squareSize, squareSize))
        elif dangersList['row'] == kingSquare[0]:
            for row in range(min(dangersList['row'], kingSquare[0]), max(dangersList['row'], kingSquare[0])):
                squaresToCover.append(pygame.Rect(row*squareSize, dangersList['column']*squareSize, squareSize, squareSize))
        #przekątne/koń
        elif dangersList['row'] != kingSquare[0] and dangersList['column'] != kingSquare[1]:
            if dangersList['piece'] == 'Knight':
                squaresToCover.append(pygame.Rect(dangersList['row']*squareSize, dangersList['column']*squareSize, squareSize, squareSize))
            else:
                pass
        return True