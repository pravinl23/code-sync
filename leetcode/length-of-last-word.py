class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        fast = slow = 0

        last = 0
        while fast < len(s):
            if s[fast] == " ":
                if fast != slow:
                    last = fast - slow
                slow = fast + 1
            fast += 1
        
        if s[fast - 1] == " ":
            return last
        else:
            return fast - slow