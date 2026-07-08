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

        # more optimized, instead of doing 3 separate passes (rows, columns, squares)
        # iterate through every square once and assign to the set
        # need to keep more hash sets e.g. hash set for every row, col, square and keep a running tab
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                currentSquare = board[r][c]
                if currentSquare == '.':
                    continue
                if (currentSquare in rows[r]
                    or currentSquare in cols[c]
                    or currentSquare in squares[(r // 3, c //3)]): # use tuple to mark the subsquare
                    return False
                else:
                    rows[r].add(currentSquare)
                    cols[c].add(currentSquare)
                    squares[(r //3, c//3)].add(currentSquare)
        
        return True
