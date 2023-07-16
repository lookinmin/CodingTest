# 게임, S3, 이분탐색

from sys import stdin

X, Y = map(int, stdin.readline().split())
Z = (Y*100)//X

if Z >= 99:
    print(-1)
else:
    res = 0
    start = 1
    end = X

    while start <= end:
        mid = (start + end) // 2
        now = ((Y + mid) * 100) // (X + mid)
        if now <= Z:        # 승률이 늘지 않음
            start = mid + 1
        else:
            res = mid
            end = mid - 1

    print(res)
