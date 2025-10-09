class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = { 0: 0, '(' : ')', '{' : '}', '[' : ']' }

        seen = [0]
        idx = 0

        for char in s:
            print(char)
            print(seen[idx])
            if char in brackets:
                seen.append(char)
                idx += 1
            elif brackets[seen[idx]] != char:
                return False
            else:
                seen.pop()
                idx -= 1
        
        if len(seen) > 1:
            return False
        return True