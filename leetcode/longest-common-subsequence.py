class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """      
        n = len(text1)
        m = len(text2)
        dp = {}
        def recurse(i, j):
            if i == n or j == m:
                return 0
            if (i, j) in dp:
                return dp[(i,j)]
            if text1[i] == text2[j]:
                dp[(i,j)] = 1 + recurse(i + 1, j + 1)
            else:
                dp[(i,j)] = max(recurse(i + 1, j), recurse(i, j + 1))
            return dp[(i, j)]


        return recurse(0, 0)