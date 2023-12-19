#The problem: 
#Print a given matrix in spiral form

#Approach:
# - Let the array have m rows and n columns
# - Visited[i][j] denotes that cell on the i-th row
# and j-th column was previously visited. 
# Our current position is (i, j), facing direction 
# dir and we want to visit m x n total cells
# - As we move through the matrix, our canditate
# next position is (ci, cj)
# - If the canditate is in bounds of the matrix and
# unvisited it become our next position, otherwise; 
# our next position is the one after performing a
# clockwise turn

#Implementation:

def spiralOrder(matrix):
    result = []

    if (len(matrix)==0):
        return result
    
    m = len(matrix)
    n = len(matrix[0])
    seen = [[0 for i in range(n)] for j in range(m)]
    di = (0, 1, 0, -1)
    dj = (1, 0, -1, 0)
    x = 0
    y = 0 
    dir = 0 

    for i in range(m*n):
        result.append(matrix[x][y])
        seen[x][y] = True
        ci = x + di[dir]
        cj = y + dj[dir] 

        if (0 <= ci and ci < m and 0 <= cj and cj < n and not(seen[ci][cj])):
            x = ci 
            y = cj
        else:
            dir = (dir+1)%4
            x += di[dir]
            y += dj[dir]
    return result
    
if __name__ == "__main__": 
    example = [[1, 2, 3, 4],
         [12, 13, 14, 5],
         [11, 16, 15, 6],
         [10, 9, 8, 7]]
    for x in spiralOrder(example):
        print(x, end = " ")
    print()

