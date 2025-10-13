class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []
        COLS = len(heights[0]) - 1
        ROWS = len(heights) - 1

        pac = set()
        atl = set()

        def dfs(r, c, prevHeight, ocean):
            if (r,c) in ocean or r < 0 or r > ROWS or c < 0 or c > COLS or heights[r][c] < prevHeight:
                return
            ocean.add((r,c))
            dfs(r + 1, c, heights[r][c], ocean)
            dfs(r - 1, c, heights[r][c], ocean)
            dfs(r, c + 1, heights[r][c], ocean)
            dfs(r, c - 1, heights[r][c], ocean)
            


        for r in range(ROWS + 1):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS, heights[r][COLS], atl)

        for c in range(COLS + 1):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS, c, heights[ROWS][c], atl)

        output = []
        for o in pac:
            if o in atl:
                output.append(o)
        
        return output