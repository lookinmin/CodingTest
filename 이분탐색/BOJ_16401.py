# 과자 나눠주기, S2, 이분 탐색

from sys import stdin

m, n = map(int, stdin.readline().split())
arr = list(map(int,stdin.readline().split()))

start = 0
end = max(arr)

cnt = 0
while start <= end:
    total = 0                   # 현재 몇개가 나왔는지
    mid = (start + end) // 2

    if mid == 0:
        total = 0
        break

    for i in arr:
        total += (i // mid)         # 현재 몇개가 나왔는 지에 추가

    if total >= m:
        cnt = max(cnt, mid)
        start = mid + 1
    else:
        end = mid-1

print(cnt)

