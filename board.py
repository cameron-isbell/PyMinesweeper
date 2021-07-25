import random
from mine import Mine

class Board:

    def __swap(self, arr, x, y):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp

    #generate a minesweeper board
    def __init__(self, in1, in2):
        self.WIDTH = 8
        self.HEIGHT = 8
        self.NUM_MINES = 10
        self.grid = [[Mine(False) for i in range(self.WIDTH)] for j in range(self.HEIGHT)]

        #number of columns we're able to choose from
        fullCols = list(range(0, self.HEIGHT))

        #a 2d array of spots we're able to choose. 
        availSpots = [[i for i in range(self.WIDTH)] for j in range(self.HEIGHT)]

        random.seed()
        #add all mines to the grid
        for i in range(0, self.NUM_MINES):
            #choose a random index from 0 -> #cols remaining, xIdx is the value 
            #ex. if fullCols = [1,2,5,6] if x = 2, xIdx = 5
            x = random.randint(0, fullCols.__len__()-1)
            xIdx = fullCols[x]

            y = random.randint(0, availSpots[xIdx].__len__()-1)
            yIdx = availSpots[xIdx][y]

            self.grid[xIdx][yIdx] = Mine(True)

            #remove this Mine as an available position
            availSpots[xIdx].pop(y)

            #if the column is empty, remove it from availSpots
            if (availSpots[xIdx].__len__() <= 0):
                fullCols.pop(x)
