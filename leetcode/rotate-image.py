class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # vertically reflect
        def reflect(m):
            n = len(m)
            for i in range(len(m) // 2):
                temp = m[len(m) - i - 1]
                m[len(m) - i - 1] = m[i]
                m[i] = temp
            

        reflect(matrix)
        def transpose(m):
            for r in range(len(m)):
                for c in range(r + 1, len(m)):
                    print(r,c)
                    temp = m[r][c]
                    m[r][c] = m[c][r]
                    m[c][r] = temp

        transpose(matrix)
        return matrix