from Grid import Grid 

print("Welcome to Tic-Tac-Terminal-Toe")
print("The long awaited Terminal based version of Tic-Tac-Toe.")
print('=======================================')

grid= Grid()

grid.displayGrid()
print('=======================================')


while grid.continueGame:
    grid.playerMove(1)
    if not grid.continueGame:
        break
    grid.playerMove(2)