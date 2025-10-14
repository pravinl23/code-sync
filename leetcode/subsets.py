class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        def backtrack(index, path):
            if index == len(nums): # reached a leaf
                output.append(path[:])
                return

            # decicison # 1 remove the element
            backtrack(index + 1, path)

            # decision # 2 add the element
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop() # pass by object reference its shared w everythign so pop

        backtrack(0, [])

        return output