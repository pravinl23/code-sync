class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)

            newStone = max(s1, s2) - min(s1, s2)
            heapq.heappush(stones, -newStone)

        if len(stones) > 0:
            return -heapq.heappop(stones)
        else:
            return 0