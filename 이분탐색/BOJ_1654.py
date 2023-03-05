# 랜선 자르기, S2, 이분탐색
from sys import stdin

k, n = map(int,stdin.readline().split())
arr = []

for _ in range(k):
    arr.append(int(stdin.readline().rstrip()))

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for x in arr:
        cnt += x // mid

    if cnt >= n :       # 랜선이 n개 보다 많으면, mid값을 올려야함
        start = mid + 1
    else:
        end = mid - 1

print(end)

