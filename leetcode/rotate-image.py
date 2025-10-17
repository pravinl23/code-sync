class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # vertically reflect
        def reflect(m):
            n = len(m)
            for i in range(n // 2):
                temp = m[n - i - 1]
                m[n - i - 1] = m[i]
                m[i] = temp
            

        reflect(matrix)
        def transpose(m):
            n = len(m)
            for r in range(n):
                for c in range(r + 1, n):
                    temp = m[r][c]
                    m[r][c] = m[c][r]
                    m[c][r] = temp

        transpose(matrix)
        return matrix