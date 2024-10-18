class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) == 1:
            return 0
        
        tmp = nums[-1] - nums[0]
        if k * 2 >= tmp:
            return 0
        else:
            return tmp - (k * 2)