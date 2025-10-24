class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        numRows = len(board)
        numCols = len(board[0])
        n = len(word)
        def dfs(r, c, idx):
            if idx == n:
                return True
            nextChar = word[idx]
            nextMove = []
            if r + 1 < numRows and board[r + 1][c] == nextChar and (r + 1, c) not in seen:
                nextMove.append([r + 1, c])
            if r - 1 >= 0 and board[r - 1][c] == nextChar and (r - 1, c) not in seen:
                nextMove.append([r - 1, c])
            if c + 1 < numCols and board[r][c + 1] == nextChar and (r, c + 1) not in seen:
                nextMove.append([r, c + 1])
            if c - 1 >= 0 and board[r][c - 1] == nextChar and (r, c - 1) not in seen:
                nextMove.append([r, c - 1])
            
            output = False
            for m in nextMove:
                seen.append((m[0],m[1]))
                output = output or dfs(m[0], m[1], idx + 1)
                seen.pop()
            return output
                
        seen = []
        for r in range(numRows):
            for c in range(numCols):
                currChar = board[r][c]
                if currChar == word[0]:
                    seen.append((r,c))
                    found = dfs(r, c, 1)
                    seen.pop()
                    if found:
                        return True
            
        return False