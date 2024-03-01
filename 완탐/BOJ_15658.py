# 연산자 끼워넣기(2), 완탐, S2
from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
op = list(map(int, stdin.readline().split()))

maxRes = -int(1e9)
minRes = int(1e9)

def dfs(idx, now):
    global maxRes, minRes

    if idx == n:
        maxRes = max(maxRes, now)
        minRes = min(minRes, now)
        return

    if op[0] > 0:
        op[0] -= 1
        dfs(idx + 1, now + nums[idx])
        op[0] += 1

    if op[1] > 0:
        op[1] -= 1
        dfs(idx + 1, now - nums[idx])
        op[1] += 1

    if op[2] > 0:
        op[2] -= 1
        dfs(idx + 1, now * nums[idx])
        op[2] += 1

    if op[3] > 0:
        op[3] -= 1
        dfs(idx + 1, int(now / nums[idx]))
        op[3] += 1

dfs(1, nums[0])

print(maxRes)
print(minRes)