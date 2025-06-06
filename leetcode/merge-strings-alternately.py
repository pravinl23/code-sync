class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = []
        k = min(len(word1), len(word2))
        for i in range(k):
            output.append(word1[i])
            output.append(word2[i])

        l = len(output) / 2
        output.append(word1[l:])
        output.append(word2[l:])
        return "".join(output)