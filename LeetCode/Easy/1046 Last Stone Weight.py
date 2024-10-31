import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            if x == y:
                continue
            else:
                heapq.heappush(maxHeap, -(y - x))
        
        if len(maxHeap) == 1:
            return -maxHeap[0]
        else:
            return 0