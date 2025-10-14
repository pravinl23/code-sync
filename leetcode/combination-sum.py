class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        outputHash = {}
        def backtracking(index, path, sum):
            if index == len(candidates):
                return
            if sum > target:
                return
            if sum == target:
                res = tuple(path[:])
                if res in outputHash:
                    return
                else:
                    outputHash[res] = 0
                    output.append(path[:])
            
            # decision #1 add it
            path.append(candidates[index])
            sum = sum + candidates[index]
            backtracking(index, path, sum)
            path.pop()
            sum = sum - candidates[index]

            # decision #2 go next num

            backtracking(index + 1, path, sum)


        backtracking(0, [], 0)
        return output