from colors import brown, white, properWhite, black
import chessBoardClass
import pygame
pygame.init()

def setUptheBoard(chessBoard: chessBoardClass.chessBoard, screen, boardPosition: list, listOfSquares: list):
    screen = pygame.display.set_mode((800, 800))
    squareSize = 100
    pygame.display.set_caption('Chess')
    for row in range(chessBoard.width):
        for column in range(chessBoard.height):
            sqr = pygame.Rect(row*squareSize, column*squareSize, squareSize, squareSize)
            listOfSquares.append(sqr)
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

    for column in range(len(boardPosition)):
        for row in range(len(boardPosition[column])):
            for square in listOfSquares:
                if square.centerx == squareSize/2+column*squareSize and square.centery == squareSize/2+row*squareSize and boardPosition[column][row] != None:
                    img = pygame.image.load(f'C:\\VSCODE\\projekt pygame\\chess\\img\\{boardPosition[column][row]}.png')
                    img = pygame.transform.smoothscale(img, (squareSize, squareSize))
                    screen.blit(img, (row*squareSize, column*squareSize))