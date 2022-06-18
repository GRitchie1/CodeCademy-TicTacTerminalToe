class Grid():
    def __init__(self):
        self.gridSize = 3
        self.grid=[[" " for i in range(self.gridSize)] for i in range(self.gridSize)]
        self.totalMoves=self.gridSize**2
        self.moves=0

    def displayGrid(self):
        for i in range(len(self.grid)):
            print(self.grid[i])

    def _checkForWin():
        if self.moves >= self.totalMoves:
            print("Game Over")

    def _verifyMove(self,x,y,player):
        if x >= self.gridSize or x < 0:
            print("X Value must be in range!")
            return None
        if y >= self.gridSize or y < 0:
            print("Y Value must be in range!")
            return None

        selectedSpace = self.grid[y][x]
        if selectedSpace != " ":
            print("Space Must be empty!")
            return None
        if player == 1:
            self.grid[y][x] = 'X'
            self.moves+=1
            return self.grid[y][x]
        elif player == 2:
            self.grid[y][x] = 'O'
            self.moves+=1
            return self.grid[y][x]
        else:
            print("Player must be either 1 or 2.")
            return None

    def playerMove(self, player):
        x_input=int(input("Enter X Index:"))
        y_input=int(input("Enter Y Index:"))
        while self._verifyMove(x_input,y_input,player) == None:
            x_input=int(input("Re-Enter X Index:"))
            y_input=int(input("Re-Enter Y Index:"))
        self.displayGrid()
        self._checkForWin()
        print('=======================================')