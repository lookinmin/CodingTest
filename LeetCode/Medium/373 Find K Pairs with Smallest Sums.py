import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        heap = []
        res = []

        for j in range(min(k, m)):
            heapq.heappush(heap, (nums1[0] + nums2[j], 0, j))
            # (값, nums1의 인덱스, num2의 인덱스)
        
        while k > 0 and heap:
            val, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < n:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            k -= 1
        
        return res
