# 소가 정보섬에 올라온 이유, S2 - 구현
from sys import stdin

# 원형 소, 연속한 네마리 품질값의 곱을 전부 더함

n, q = map(int, stdin.readline().split())
cows = list(map(int, stdin.readline().split()))
nums = list(map(int, stdin.readline().split()))

dp = [0] * n

for i in range(n):
    dp[i] = cows[i] * cows[i - 1] * cows[i - 2] * cows[i - 3]

total = sum(dp)

for num in nums:
    num -= 1
    for i in range(4):
        new_idx = (num + i) % n
        dp[new_idx] = -dp[new_idx]
        total += 2 * dp[new_idx]
    
    print(total)