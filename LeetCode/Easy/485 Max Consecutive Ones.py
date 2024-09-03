class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            if num == 0:
                res.append(cnt)
                cnt = 0
        res.append(cnt)
        
        return max(res)