class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for idx, num in enumerate(nums):
            if left == (total - left - num):
                return idx
            left += num
        return -1