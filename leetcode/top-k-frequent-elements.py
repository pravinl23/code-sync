class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        l = []
        for num, count in a.items():
            l.append([-count, num])
        
        res = []
        heapq.heapify(l)
        for i in range(k):
            res.append(heapq.heappop(l)[1])

        return res