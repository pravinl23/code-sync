class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        numRows = len(matrix)
        numCols = len(matrix[0])
        # extra marker for col
        extC = 1

        # mark first row and col
        for r in range(numRows):
            if matrix[r][0] == 0:
                extC = 0
            for c in range(1, numCols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0 
                    matrix[0][c] = 0


        for r in range(1, numRows):
            for c in range(1, numCols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # case for zeroing out first row
        if matrix[0][0] == 0:
            for c in range(numCols):
                matrix[0][c] = 0

        # zero out first col
        if extC == 0:
            for r in range(numRows):
                matrix[r][0] = 0