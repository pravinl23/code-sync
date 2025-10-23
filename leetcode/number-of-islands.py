class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            if grid[r][c] == '1':
                grid[r][c] = '0'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        counter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '0':
                    continue
                elif grid[row][col] == '1':
                    dfs(row, col)
                    counter += 1
        return counter