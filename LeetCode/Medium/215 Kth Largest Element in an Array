import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, -num)
        
        for i in range(k-1):
            heapq.heappop(q)
        return(-q[0])