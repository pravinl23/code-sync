class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {'(' : ')', '{' : '}', '[' : ']' }

        seen = []
        for char in s:
            if char in brackets:
                seen.append(char)
            elif not seen or brackets[seen[-1]] != char:
                return False
            else:
                seen.pop()

        return not seen