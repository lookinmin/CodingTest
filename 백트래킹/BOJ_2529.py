# 부등호, S1, 완탐, 백트래킹
from sys import stdin

k = int(stdin.readline())
arr = list(stdin.readline().split())
visited = [0] * 10
res_max = ""
res_min = ""

def check(i,j,k):
    if k == '<':
        return i < j
    else:
        return i > j

def solve(idx, s):
    global res_min, res_max

    if idx == k+1:
        if len(res_min)==0:
            res_min = s
        else:
            res_max = s
        return
    for i in range(10):
        if visited[i] == 0:
            if idx == 0 or check(s[-1], str(i), arr[idx-1]):
                visited[i] = 1
                solve(idx+1, s + str(i))
                visited[i] = 0

solve(0, "")
print(res_max)
print(res_min)