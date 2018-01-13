def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row = len(grid)
    col = len(grid[0])
    peri = 0
    udlr = [(-1,0), (1,0), (0,1), (0,-1)]
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                count = 0
                for direc in udlr:
                    i_, j_ = i+direc[0], j+direc[1]
                    if (0 <= i_ < row) and (0 <= j_ < col) and grid[i_][j_] == 1:
                        count+=1
                peri += 4-count
    return peri


    

if __name__ == '__main__':
	print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))