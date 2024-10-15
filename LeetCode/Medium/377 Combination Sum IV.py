class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = dict()
        
        def dfs(remaining):
            if remaining == 0:
                # 더 이상 남은 값이 없음 == 조합 완성
                return 1
            if remaining in memo:
                # 이미 계산된 값이 있음 -> 이미 특정 값을 만드는 조합이 존재
                return memo[remaining]
                # 해당 값을 꺼내서 리턴

            total = 0
            for num in nums:
                if remaining - num >= 0:
                    total += dfs(remaining - num)
            
            memo[remaining] = total
            # 특정 값을 만드는데 필요한 조합의 수를 memo에 저장
            return total
        
        return dfs(target)
