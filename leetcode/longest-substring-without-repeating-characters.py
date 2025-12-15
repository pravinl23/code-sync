class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        maxsofar = 0
        seen = set()
        while r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                r += 1
                maxsofar = max(r - l, maxsofar)

        return maxsofar