class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        movesList = [(1,0), (-1,0), (0,1), (0,-1)]
        res = []

        def dfs(r, c, t):            
            w = t.pop(".", None)
            if w:
                res.append(w)

            emptied = False
            if not t:
                emptied = True
            for moves in movesList:
                nr, nc = r + moves[0], c + moves[1]
                if 0 <= nr < numRows and 0 <= nc < numCols and board[nr][nc] != "#" and board[nr][nc] in t:
                    tmp = board[nr][nc]
                    board[nr][nc] = "#"
                    child = dfs(nr, nc, t[tmp])
                    board[nr][nc] = tmp

                    if child:
                        t.pop(tmp, None)

            return not t

            return



        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["."] = w
            
        #print(trie)
        numRows = len(board)
        numCols = len(board[0])

        for r in range(numRows):
            for c in range(numCols):
                if board[r][c] in trie:
                    tmp = board[r][c]
                    board[r][c] = "#"
                    emptied = dfs(r, c, trie[tmp])
                    board[r][c] = tmp

                    if emptied:
                        trie.pop(tmp, None)
        
        #print(trie)

        return res