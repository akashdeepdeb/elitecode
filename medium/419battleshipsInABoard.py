class Solution(object):
    def recurse(self, board, r, c, rows, cols):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == '.':
            return 
        if board[r][c] == 'X':
            board[r][c] = '.'
        self.recurse(board, r+1, c, rows, cols)
        self.recurse(board, r-1, c, rows, cols)
        self.recurse(board, r, c+1, rows, cols)
        self.recurse(board, r, c-1, rows, cols)

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i, row in enumerate(board):
            for j, dot_cross in enumerate(row):
                if dot_cross == 'X':
                    self.recurse(board, i, j, len(board), len(board[0]))
                    count += 1
        return count
    
    #alternatively, check the first occurance of the X and discard all others by continually checking the top, left element every 
    #time - if there is an X at the top/left, don't increase the counter because you have already seen this battleship before
        


# if __name__ == '__main__':
# 	test = [['X','.','.','X'], 
# 		  	['.','.','.','X'], 
# 		    ['.','.','.','X']]
# 	print(countBattleships(test))
        