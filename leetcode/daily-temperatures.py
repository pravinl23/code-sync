class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0 for i in range(len(temperatures))]
        monostack = []
        for i in range(len(temperatures)):
            if not monostack:
                monostack.append(i)
                continue
            while monostack and temperatures[i] > temperatures[monostack[-1]]:
                idx = monostack.pop()
                res[idx] = i - idx
            monostack.append(i)

        return res