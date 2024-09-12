class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        asc = sorted(nums)
        desc = sorted(nums, reverse = True)

        if nums == asc or nums == desc:
            return True
        else:
            return False
        