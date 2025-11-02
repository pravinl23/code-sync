class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {}
        for i in range(9):
            rows[i] = set()
        cols = {}
        for i in range(9):
            cols[i] = set()
        square = {}
        for i in range(3):
            for j in range(3):
                square[(i, j)] = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    gx = r // 3
                    gy = c // 3
                    if board[r][c] in square[(gx, gy)]:
                        return False
                    square[(gx, gy)].add(board[r][c])

                    if board[r][c] in rows[r]:
                        return False
                    rows[r].add(board[r][c])

                    if board[r][c] in cols[c]:
                        return False
                    cols[c].add(board[r][c])


        return True