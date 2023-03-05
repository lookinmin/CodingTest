# 한 봉지안에 들어가는 떡의 총 길이는 맞춰줌
# 기준 높이 : H
# 요청한 길이 : M
# H의 최대값은?
# N = 떡의 개수, M = 요청한 떡의 길이

from sys import stdin

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

start = 0
end = max(arr)
res = 0

while start <= end:
    total = 0
    mid = (start+end)//2
    for x in arr:
        if x > mid:
            total += x - mid

    if total < M:
        end = mid - 1

    else:
        res = mid
        start = mid+1

print(res)
