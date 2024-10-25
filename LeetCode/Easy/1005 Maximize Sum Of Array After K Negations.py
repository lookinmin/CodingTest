from typing import List
import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k > 0:
            num = heapq.heappop(nums)
            num *= -1
            heapq.heappush(nums, num)
            k -= 1
        return sum(nums)