class Grid():
    def __init__(self):
        self.gridSize = 3
        self.grid=[[" " for i in range(self.gridSize)] for i in range(self.gridSize)]
        self.totalMoves=self.gridSize**2
        self.moves=0

    def displayGrid(self):
        for i in range(len(self.grid)):
            print(self.grid[i])

    def checkForWin():
        if self.moves >= self.totalMoves:
            print("Game Over")

    def playMove(self,x,y,player):
        selectedSpace = self.grid[y][x]
        if selectedSpace != " ":
            return None
        if player == 1:
            self.grid[y][x] = 'X'
            return self.grid[y][x]
        elif player == 2:
            self.grid[y][x] = 'O'
            return self.grid[y][x]
        else:
            return None
        self.moves+=1
        