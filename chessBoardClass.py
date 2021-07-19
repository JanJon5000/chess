from pprint import pprint
class chessBoard:
    def __init__(self):
        possiblePieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        self.width = 8; self.height = 8
        self.size = (self.width, self.height)
        self.clicked = None
        self.boardModel = []
        
        for row in range(self.width):
            line = []
            for _ in range(self.height):
                line.append(None)
            self.boardModel.append(line)

        self.boardModel[0] = ['black' + piece.capitalize() for piece in possiblePieces]
        self.boardModel[-1] = ['white' + piece.capitalize() for piece in possiblePieces]
        self.boardModel[1] = ['blackPawn' for _ in range(self.width)]
        self.boardModel[-2] = ['whitePawn' for _ in range(self.width)]