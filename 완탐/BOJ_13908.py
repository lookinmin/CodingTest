# 비밀번호, S2
from sys import stdin

n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
res = 0

def dfs(picked):
    global res
    if len(picked) == n:
        for num in nums:
            if num not in picked:
                break
        else:
            res += 1
        return

    for i in range(10):
        picked.append(i)
        dfs(picked)
        picked.pop()

for i in range(10):
    picked = []
    picked.append(i)
    dfs(picked)
    picked.pop()

print(res)