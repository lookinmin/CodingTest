# 풍선공장, S2, 이분탐색

from sys import stdin

n,m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

start = 0
end = max(arr) * m      # 가장 오래걸리는 사람이 전부 만들때 걸리는 총 시간
res = 0
while start <= end:
    mid = (start+end) // 2          # mid는 만들때 걸리는 시간으로 생각
    cnt = 0             # 몇개 만들었는지

    for i in arr:
        cnt += mid // i     # 시간대비로 나눠주기

    if cnt < m:         # 만든 개수가 원하는 m 보다 적으면
        start = mid + 1 # 시작 점을 올려서
    else:
        res = mid
        end = mid -1

print(res)

