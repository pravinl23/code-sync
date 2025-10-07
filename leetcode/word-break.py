class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        actualDict = {}
        maxlen = 0
        for word in wordDict:
            maxlen = max(maxlen, len(word))
            actualDict[word] = True
        
        dp = {}

        output = False
        def Search(searchS):
            if searchS in dp:
                return dp[searchS]

            if searchS == "":
                return True

            for i in range(1, len(searchS) + 1):
                substr = searchS[:i]
                if len(substr) > maxlen:
                    break
                if substr in actualDict:
                    rest = Search(searchS[i:])
                    if rest:
                        dp[searchS] = True
                        return True

            dp[searchS] = False
            return False

        return Search(s)