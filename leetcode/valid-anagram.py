class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dp = {}
        for index, ch in enumerate(s):
            if ch not in dp:
                dp[ch] = []

            dp[ch].append(index)
        
        for ch in t:
            if ch not in dp:
                return False
            if dp[ch] == []:
                return False
            dp[ch].pop()

        return True