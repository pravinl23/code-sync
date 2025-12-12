class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        unable = set()
        numRows = len(board)
        numCols = len(board[0])
        DIRS = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c):
            for nr, nc in DIRS:
                nr, nc = nr + r, nc + c
                if 0 <= nr < numRows and 0 <= nc < numCols and board[nr][nc] == "O" and (nr, nc) not in unable:
                    unable.add((nr, nc))
                    dfs(nr, nc)

        
        # check borders
        for r in range(0, numRows):
            if board[r][numCols - 1] == "O":
                unable.add((r, numCols - 1))
                dfs(r, numCols - 1)
            if board[r][0] == "O":
                unable.add((r, 0))
                dfs(r, 0)

        for c in range(0, numCols):
            if board[numRows - 1][c] == "O":
                unable.add((numRows - 1, c))
                dfs(numRows - 1, c)
            if board[0][c] == "O":
                unable.add((0, c))
                dfs(0, c)


        for r in range(numRows):
            for c in range(numCols):
                if (r, c) not in unable:
                    board[r][c] = "X"