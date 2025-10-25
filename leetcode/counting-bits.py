class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        res = [0,1]
        dp = {0:0, 1:1}
        digit = 1
        for i in range(2, n + 1):
            if digit * 2 == i:
                digit = i
            ans = 1 + dp[i - digit]
            res.append(ans)
            dp[i] = ans
 
        return res