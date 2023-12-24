#Idea simple: Check every cell 
# If cell has first character then one by one we try all 8 dirs
# from that cell for  a match
# We use 2 array x[] and y[] to find next move in all 8 dirs


class GFG:
    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [(-1, 0), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1), (0, 1), (0, -1)]
    
    def search2D(self, grid, row, col, word):
        if grid[row][col] != word[0]:
            return False
        
        for x, y in self.dir: 
            rd, cd = row+x, col+y
            flag = True


            for k in range(1, len(word)):
                if (0 <= rd < self.R and 0 <= cd < self.C and word[k] == grid[rd][cd]):
                    rd += x
                    cd += y
                else:
                    flag = False
                    break
            if flag:
                return True
        return False
        
    def patternSearch(self, grid, word):
        self.R = len(grid)
        self.C = len(grid[0])

        for row in range(self.R):
            for col in range(self.C):
                if self.search2D(grid, row, col, word):
                    print("pattern found at " + str(row) + ", " + str(col))
    

if __name__ == '__main__':
    grid = ["EXAMPLEOFGRID",
            "NICEEXAMPLEEE",
            "THIRDEXAMPLEE"]
    
    gfg = GFG()

    gfg.patternSearch(grid, "EXAMPLE")
    print('')
    gfg.patternSearch(grid, "EE")


