from colors import brown, white, properWhite, black
import chessBoardClass
import pygame
pygame.init()

def setUptheBoard(chessBoard: chessBoardClass.chessBoard, screen, boardPosition: list, listOfSquares: list):
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Chess')
    for row in range(chessBoard.width):
        for column in range(chessBoard.height):
            sqr = pygame.Rect(row*50, column*50, 50, 50)
            listOfSquares.append(sqr)
            if row % 2 == 0:
                if column % 2 != 0:
                    pygame.draw.rect(screen, brown, sqr)
                else:
                    pygame.draw.rect(screen, white, sqr)___
            else:
                if column % 2 != 0:
                    pygame.draw.rect(screen, white, sqr)
                else:
                    pygame.draw.rect(screen, brown, sqr)

    for column in range(len(boardPosition)):
        for row in range(len(boardPosition[column])):
            for square in listOfSquares:
                if square.centerx == 25+column*50 and square.centery == 25+row*50 and boardPosition[column][row] != None:
                    img = pygame.image.load(f'C:\\VSCODE\\projekt pygame\\chess\\img\\{boardPosition[column][row]}.png')
                    screen.blit(img, (row*50+15, column*50+10))