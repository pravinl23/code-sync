class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(path, localnums):
            if len(path) == len(nums):
                res.append(path[:])

            for num in localnums:
                path.append(num)
                d = localnums[:]
                d.remove(num)
                backtracking(path, d)
                path.pop()
            
        backtracking([],nums)
        return res