class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k
        now = sum(nums[:k])
        res = now

        for i in range(k, len(nums)):
            now += nums[i] - nums[i - k]
            res = max(res, now)
        
        return res / k