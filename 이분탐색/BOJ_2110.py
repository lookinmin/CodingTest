# 공유기 설치, G4, 이분탐색
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치

from sys import stdin

n, c = map(int, stdin.readline().split())
arr = []

for _ in range(n):
    arr.append(int(stdin.readline().rstrip()))

arr.sort()

start = 1
end = arr[-1] - arr[0]          # ex 8
res = 0

# 1. 앞 집부터 공유기 설치
# 2. 설치할 수 있는 공유기 개수가 c개를 넘어가면 더 넓게 설치할 수 있다는 이야기 이므로 설치거리를 mid + 1로 설정하여 다시 앞집부터 설치.
# 3. c개를 넘어가지 않는다면 더 좁게 설치해야 한다는 이야기 이므로 mid - 1로 설정.

while start <= end:
    mid = (start + end) // 2        # 공유기를 설치할 거리의 기준
    tmp = arr[0]
    cnt = 1

    for i in range(1, n):
        if arr[i] >= tmp + mid:
            cnt += 1
            tmp = arr[i]
    # 현재 집에서 다음 집의 거리가 mid를 초과한다면 공유기 설치 가능
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)