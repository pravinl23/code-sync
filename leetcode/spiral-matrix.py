class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        n = (bottom + 1) * (right + 1)
        

        n = (bottom + 1) * (right + 1)
        res = []
        r, c = 0, 0
        res.append(matrix[r][c])
        while left <= right and top <= bottom:
            print(left, right, top, bottom)
            # right
            while c < right:
                c += 1
                res.append(matrix[r][c])
            top += 1
            # down
            while r < bottom:
                r += 1
                res.append(matrix[r][c])
            right -= 1
            # left
            while c > left:
                c -= 1
                res.append(matrix[r][c])
            bottom -= 1
            # up
            while r > top:
                r -= 1
                res.append(matrix[r][c])
            left += 1

        return res[:n]