class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        numRows = len(matrix)
        numCols = len(matrix[0])
        for r in range(numRows):
            for c in range(numCols):
                if matrix[r][c] == 0:
                    # replace row
                    for i in range(0, numRows):
                        if matrix[i][c] == 0:
                            continue
                        else:
                            matrix[i][c] = 'a'
                    # replace col
                    for i in range(0, numCols):
                        if matrix[r][i] == 0:
                            continue
                        else:
                            matrix[r][i] = 'a'

        for r in range(numRows):
            for c in range(numCols):
                if matrix[r][c] == 'a':
                    matrix[r][c] = 0

        
        return matrix