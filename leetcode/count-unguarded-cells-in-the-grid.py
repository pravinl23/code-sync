class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        board = [["." for i in range(n)] for j in range(m)]
        #print(board)

        for w in walls:
            board[w[0]][w[1]] = "W"
        for g in guards:
            board[g[0]][g[1]] = "G"

        #print(board)
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        for g in guards:
            for dx, dy in DIRS:
                x = g[0] + dx
                y = g[1] + dy
                while 0 <= x < m and 0 <= y < n and board[x][y] != "W" and board[x][y] != "G":
                    board[x][y] = "VISITED"
                    x += dx
                    y += dy
        #print(board)

        counter = 0
        for r in range (len(board)):
            for c in range (len(board[0])):
                if board[r][c] == ".":
                    counter += 1

        return counter