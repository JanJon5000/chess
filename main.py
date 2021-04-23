import pygame
import chessBoardClass
pygame.init()

chessBoard = chessBoardClass.chessBoard()
screen = pygame.display.set_mode((400, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
