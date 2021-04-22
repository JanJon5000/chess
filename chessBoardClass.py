class chessBoard:
    def __init__(self):
        self.width = 8; self.height = 8
        self.size = (self.width, self.height)
        self.clicked = None
        self.boardModel = []

        for _ in range(self.width):
            line = []
            for a in range(self.height):
                line.append(None)
            self.boardModel.append(line)
        
