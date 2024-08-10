class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        now = nums[0]
        res = float('inf')

        while r <= len(nums) - 1:
            if now < target:
                r += 1
                if r <= len(nums) - 1:
                    now += nums[r]
            else:
                res = min(res, r - l + 1)
                now -= nums[l]
                l += 1
        
        if res == float('inf'):
            return 0
        return res