# 가장 긴 바이토닉 부분 수열, G4, DP - 재시도

from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [1] * n
dp2 = [1] * n

# 계속 증가만 하거나
# 계속 감소만 하거나
# 증가하다 감소하거나

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)       # 증가하는것중에 제일 긴거

arr.reverse()   # 거꾸로 돌리고 다시 증가하는거 찾으면

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)        # 감소하는 것중에 가장 긴거 찾을 수 있음

dp2.reverse()

res = [1] * n

for i in range(n):
    res[i] = dp[i] + dp2[i]

print(max(res) - 1)         # 증가하는 수의 마지막, 감소하는 수의 처음이 겹침