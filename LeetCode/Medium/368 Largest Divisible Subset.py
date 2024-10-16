class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)       
        dp = [1] * n
        prev = [-1] * n

        max_idx = 0
        # 가장 큰 부분집합의 마지막 원소 인덱스

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            
            if dp[i] > dp[max_idx]:
                max_idx = i
        
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = prev[max_idx]
        
        return res[::-1]