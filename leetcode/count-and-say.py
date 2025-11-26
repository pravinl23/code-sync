class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)

        s = ""
        i = 0
        while i < len(prev):
            
            count = 1
            while i < len(prev) - 1 and prev[i] == prev[i + 1]:
                i += 1
                count += 1
            s += str(count) + prev[i]
            i += 1
        

        return s