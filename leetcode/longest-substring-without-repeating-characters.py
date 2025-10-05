class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        maxlen = 0
        current = 0
        oldidx = 0
        for i in range(len(s)):
            char = s[i]
            if char in seen:
                maxlen = max(current, maxlen)
                current = i - seen[char] - 1
                for j in range(oldidx,seen[char]+1):
                    oldidx += 1
                    if j in seen:
                        del seen[seen[j]]
                        del seen[j]
            current += 1
            seen[char] = i
            seen[i] = char
        maxlen = max(current,maxlen)

        return maxlen