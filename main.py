from Grid import Grid 

print("Welcome to Tic-Tac-Terminal-Toe")
print("The long awaited Terminal based version of Tic-Tac-Toe.")

grid= Grid()

grid.displayGrid()
print('=======================================')


while True:
    grid.playerMove(1)
    grid.playerMove(2)