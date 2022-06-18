from Grid import Grid 

print("Welcome to Tic-Tac-Terminal-Toe")
print("The long awaited Terminal based version of Tic-Tac-Toe.")

grid= Grid()

grid.displayGrid()
print('=======================================')

grid.playMove(0,0,1)
grid.displayGrid()
print('=======================================')

grid.playMove(0,1,2)
grid.displayGrid()
print('=======================================')