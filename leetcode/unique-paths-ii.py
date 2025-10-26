class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        numRows = len(obstacleGrid)
        numCols = len(obstacleGrid[0])

        DIRS = [(1, 0), (0, 1)]


        dp = {}

        def dfs(r, c):
            #obscure edge cases
            if (r,c) in dp:
                return dp[(r,c)]
            if obstacleGrid[r][c] == 1:
                dp[(r,c)] = 0
                return 0
            if r == numRows - 1 and c == numCols - 1:
                dp[(r,c)] = 1
                return 1
            
            m = []
            for d in DIRS:
                nr = r + d[0]
                nc = c + d[1]
                if nr < numRows and nc < numCols and obstacleGrid[nr][nc] != 1:
                    m.append((nr, nc))

            if len(m) == 2:
                ans = dfs(m[0][0], m[0][1]) + dfs(m[1][0], m[1][1])
                dp[(r,c)] = ans
                return ans
            elif len(m) == 1:
                ans = dfs(m[0][0], m[0][1])
                dp[(r,c)] = ans
                return ans
            else:
                dp[(r,c)] = 0
                return 0


        return dfs(0, 0)