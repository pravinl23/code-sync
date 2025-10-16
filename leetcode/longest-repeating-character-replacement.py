import string

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        charMap = {ch: 0 for ch in string.ascii_uppercase}
    
        left = 0
        right = 0

        while right < len(s):
            charMap[s[right]] += 1
            
            maxChar = 0
            for c in charMap:
                maxChar = max(maxChar, charMap[c])
            # sliding window - maxchar
            if (right - left + 1) - maxChar > k:
                charMap[s[left]] -= 1
                left += 1
                right += 1
            else:
                right += 1

        return right - left