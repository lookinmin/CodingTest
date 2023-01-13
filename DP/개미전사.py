# dp 예제
# 개미전사
# 인접 창고 연속적으로 선택 불가능, 얻을 수 있는 식량의 최댓값 구하라

n = int(input())
arr = list(map(int, input().split()))
# ai = max(ai-1, ai-2 + k)
dp = [0] * 100  # n <= 100

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])

print(dp[n-1])

