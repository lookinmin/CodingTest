class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums) - 1):
            res = max(res, abs(nums[i] - nums[i + 1]))
        
        return res