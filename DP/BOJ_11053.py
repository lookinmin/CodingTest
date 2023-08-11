# 가장 긴 증가하는 부분수열, S2, DP-재시도
# LIS

from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

dp = [1] * n

for i in range(1, n):   # i가 뒤에꺼
    for j in range(i):  # j가 이전꺼
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
# 시간복잡도 O(n^2)

# for i in range(n-1):
#     for j in range(1, n):
#         if arr[i] < arr[j]:
#             dp[j] = dp[j-1] + 1

print(max(dp))