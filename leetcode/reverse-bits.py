class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        divide = 2 ** 31
        
        output = []
        for _ in range(32):
            if n >= divide:
                n -= divide
                output.append(1)
            else:
                output.append(0)
            divide /= 2

        res = 0
        for i in range(32):
            res += (2 ** i) * output[i]
        return res