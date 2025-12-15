class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        count[0] += 1 # prefixsum : counter
        sumsofar = 0

        for n in nums:
            sumsofar += n
            need = sumsofar - k
            count[sumsofar] += 1
            res += count[need]
            
        return res