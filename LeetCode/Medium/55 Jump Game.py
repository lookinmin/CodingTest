class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0

        for num in nums:
            if gas < 0:
                return False
            elif num > gas:
                gas = num
            gas -= 1
        
        return True