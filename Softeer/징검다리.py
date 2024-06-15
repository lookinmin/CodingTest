from sys import stdin
# Longest Increase Sequence

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:  # 이전 값보다 크면
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

#-------------------------- bisect 풀이 -------------------------
from sys import stdin
import bisect
# Longest Increase Sequence

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [arr[0]]

for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        # bisect_left(arr, x) : arr가 정렬되어있다는 가정 하에, x가 들어갈 인덱스 반환
        dp[idx] = arr[i]

print(len(dp))