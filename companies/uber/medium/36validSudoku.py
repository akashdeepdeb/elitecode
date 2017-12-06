def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #check for rows
        for i in range(9):
            row = board[i]
            allNums = [0 for _ in range(10)]
            for num in row:
                if num != '.':
                    allNums[int(num)]+=1
                    if allNums[int(num)] > 1:
                        return False

        #check for columns
        for i in range(9):
            col = []
            allNums = [0 for _ in range(10)]
            for j in range(9):
                col.append(board[j][i])
            for num in col:
                if num != '.':
                    allNums[int(num)]+=1
                    if allNums[int(num)] > 1:
                        return False

        #check for box
        for i in range(3):
            for j in range(3):
                sr, sc = 3*i, 3*j
                allNums = [0 for _ in range(10)]
                box = []
                for m in range(3):
                    for n in range(3):
                        box.append(board[sr+m][sc+n])
                for num in box:
                    if num != '.':
                        allNums[int(num)]+=1
                        if allNums[int(num)] > 1:
                            return False
        return True

if __name__ == '__main__':
    test1 = [['5','3','.','.','7','.','.','.','.'],
            ['6','.','.','1','9','5','.','.','.'],
            ['.','9','8','.','.','.','.','6','.'],
            ['8','.','.','.','6','.','.','.','3'],
            ['4','.','.','8','.','3','.','.','1'],
            ['7','.','.','.','2','.','.','.','6'],
            ['.','6','.','.','.','.','2','8','.'],
            ['.','.','.','4','1','9','.','.','5'],
            ['.','.','.','.','8','.','.','7','9']]

    test2 = [[".",".",".",".","5",".",".","1","."],
             [".","4",".","3",".",".",".",".","."],
             [".",".",".",".",".","3",".",".","1"],
             ["8",".",".",".",".",".",".","2","."],
             [".",".","2",".","7",".",".",".","."],
             [".","1","5",".",".",".",".",".","."],
             [".",".",".",".",".","2",".",".","."],
             [".","2",".","9",".",".",".",".","."],
             [".",".","4",".",".",".",".",".","."]]
    print(isValidSudoku(test2))
