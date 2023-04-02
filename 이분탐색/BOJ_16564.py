# 히오스 프로게이머, S1, 이분탐색

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = [ int(input()) for _ in range(n)]

start = min(arr)
end = start + k     # 가장 작은 값만 t만큼 올려주는 경우

res = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0

    for i in arr:
        if mid > i:
            tmp += (mid - i)

    if tmp <= k:
        start = mid + 1
        res = max(mid, res)
    else:
        end = mid - 1

print(res)