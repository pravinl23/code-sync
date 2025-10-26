class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        def dfs(r, c, t, wordSoFar):
            #print(wordSoFar)
            movesList = [(1,0), (-1,0), (0,1), (0,-1)]
            if "END" in t and t["END"] is True:
                res.append(wordSoFar)
                t["END"] = False
            for moves in movesList:
                nr, nc = r + moves[0], c + moves[1]
                if 0 <= nr < numRows and 0 <= nc < numCols and (nr, nc) not in seen and board[nr][nc] in t:
                    seen.add((nr, nc))
                    dfs(nr, nc, t[board[nr][nc]], wordSoFar + board[nr][nc])
                    seen.remove((nr, nc))
            return



        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["END"] = True
            
        #print(trie)
        numRows = len(board)
        numCols = len(board[0])

        for r in range(numRows):
            for c in range(numCols):
                if board[r][c] in trie:
                    seen = set()
                    seen.add((r,c))
                    dfs(r, c, trie[board[r][c]], board[r][c])
                    seen.remove((r,c))
        
        #print(trie)

        return res