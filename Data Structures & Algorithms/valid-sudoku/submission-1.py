class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input: board where len(board) = num rows, len(board[0]) = num cols
        # output: boolean valid or not
        # valid if contains 1-9 no duplicates (row, col)
        # each 3x3 sub-box contain 1-9 no duplicates
        # board does not need to be FULL e.g. can have empty entries '.' (dot)
        # assume that if not . is a digit from 1-9 (no malformed entries)

        # two components: iteration (col, row, subbox)
        # also keep counter for 1-9 uniqueness

        # time is O(n^s) since iterate through constant times through sudoku board, where n is the number of rows in the grid

        # check rows
        for row in range(0, 9):
            counter = set() # hash set for uniqueness, reset on every new row
            for col in range(0, 9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in counter:
                    return False
                else:
                    counter.add(board[row][col])
        
        # check columns
        for col in range(0, 9):
            counter = set() # hash set for uniqueness, reset on every new row
            for row in range(0, 9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in counter:
                    return False
                else:
                    counter.add(board[row][col])
        # check subboxes
        # how can we iterate through the subsquares
        # use floor(row/3), floor(col/3) to identify which subbox
        for square in range(0,9):
            counter = set()
            for i in range(0, 3):
                for j in range(0,3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in counter:
                        return False
                    else:
                        counter.add(board[row][col])


        return True # if we hit this, then everything was valid
