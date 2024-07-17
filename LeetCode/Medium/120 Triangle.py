from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        k = len(triangle)
        dp = triangle[-1][:]
        # 마지막 row 복사

        for i in range(k - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]
    
    # ---------------------------------------------------

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        k = len(triangle)

        for i in range(k - 2, -1, -1):      # 가장 밑에서 한 칸 위부터 시작
            for j in range(len(triangle[i])):
                tmp = min(triangle[i + 1][j], triangle[i + 1][j + 1])       # 아래 2개 중 작은거 선택
                cur = triangle[i][j]            # 현재값이랑 더함
                triangle[i][j] = cur + tmp      
                # 최신화
    
        return triangle[0][0]