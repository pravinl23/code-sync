class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = {}

        def recurse(currstr):
            if currstr in dp:
                return dp[currstr]
            if len(currstr) == 0:
                dp[currstr] = 1
                return 1
            if currstr[0] == '0':
                return 0
            if len(currstr) == 1:
                dp[currstr] = 1
                return 1

            ones = int(currstr[len(currstr) - 1])
            tens = int(currstr[len(currstr) - 2])
            total = tens * 10 + ones
            
            dp[currstr] = 0
            if ones != 0:
                dp[currstr] += recurse(currstr[:-1])
            if 10 <= total <= 26:
                dp[currstr] += recurse(currstr[:-2])
            return dp[currstr]


        return recurse(s)