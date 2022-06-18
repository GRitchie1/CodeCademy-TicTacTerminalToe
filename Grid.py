import re


class Grid():
    def __init__(self):
        self.gridSize = 3
        self.grid=[[" " for i in range(self.gridSize)] for i in range(self.gridSize)]
        self.totalMoves=self.gridSize**2
        self.moves=0
        self.continueGame = True

    def displayGrid(self):
        for i in range(len(self.grid)):
            print(self.grid[i])

    def _checkForWin(self):
        for row in self.grid:                                           #Check Rows
            if row[0]==row[1]==row[2]:
                if row[0]=="X":
                    return "Player 1 Wins"
                if row[0]=="O":
                    return "Player 2 Wins"
        for i in range(self.gridSize):                                  #Check columns
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                if self.grid[0][i]=="X":
                    return "Player 1 Wins"
                if self.grid[0][i]=="O":
                    return "Player 2 Wins"
        
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:       #Check diagonals
            if self.grid[0][0]=="X":
                    return "Player 1 Wins"
            if self.grid[0][0]=="O":
                return "Player 2 Wins"
        
        if self.grid[2][0] == self.grid[1][1] == self.grid[0][2]:
            if self.grid[2][0]=="X":
                    return "Player 1 Wins"
            if self.grid[2][0]=="O":
                return "Player 2 Wins"
                
        if self.moves >= self.totalMoves:
            return "Game Over - Draw"
        return None

    def _verifyMove(self,x,y,player):
        x=x-1
        y=y-1
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
        x_input=int(input(f"Enter Column {[i+1 for i in range(self.gridSize)]}: "))
        y_input=int(input(f"Enter Row {[i+1 for i in range(self.gridSize)]}: "))
        while self._verifyMove(x_input,y_input,player) == None:
            x_input=int(input(f"Re-Enter Column {[i+1 for i in range(self.gridSize)]}: "))
            y_input=int(input(f"Re-Enter Row {[i+1 for i in range(self.gridSize)]}: "))
        self.displayGrid()
        if self._checkForWin():
            print(self._checkForWin())
            self.continueGame=False
        print('=======================================')