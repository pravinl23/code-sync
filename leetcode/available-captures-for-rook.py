class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        RookR, RookC = None, None
        for r in range(8):
            for c in range(8):
                if board[r][c] == "R":
                    RookR = r
                    RookC = c
                    break

        counter = 0

        for r in range(RookR, 8):
            if board[r][RookC] == 'p':
                counter += 1
                break
            elif board[r][RookC] == 'B':
                break
        for r in range(RookR, -1, -1):
            if board[r][RookC] == 'p':
                counter += 1
                break
            elif board[r][RookC] == 'B':
                break
        for c in range(RookC, 8):
            if board[RookR][c] == 'p':
                counter += 1
                break
            elif board[RookR][c] == 'B':
                break
        for c in range(RookC, -1, -1):
            if board[RookR][c] == 'p':
                counter += 1
                break
            elif board[RookR][c] == 'B':
                break

        return counter