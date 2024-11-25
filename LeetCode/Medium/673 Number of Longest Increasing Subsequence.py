class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 기본적 LIS
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n  # LIS의 갯수 저장

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                        # 더 긴 LIS 발견, cnt[i] 초기회
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
                        # 같은 길이 LIS 추가 발견
                        # cnt[i]에 cnt[j] 값 추가
        
        max_len = max(dp)
        # 가장 긴 LIS 길이

        res = 0
        for i in range(n):
            if dp[i] == max_len:
                res += cnt[i]
        
        return res