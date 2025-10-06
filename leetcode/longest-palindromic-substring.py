class Solution(object):
    max = 0
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestP = ""
        lengthP = 0
        l = len(s)
        for i in range(l):
            left = i
            right = i +1
            while (left >= 0 and right < l) and (s[left] == s[right]):
                if (right - left + 1) >= lengthP:
                    lengthP = right - left + 1
                    longestP = s[left:right+1]
                right += 1
                left -= 1
            left = i
            right = i
            while (left >= 0 and right < l) and (s[left] == s[right]):
                if (right - left + 1) >= lengthP:
                    lengthP = right - left + 1
                    longestP = s[left:right+1]
                right += 1
                left -= 1

        return longestP