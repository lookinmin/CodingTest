# 행운의 문자열, S1
from sys import stdin

string = stdin.readline().rstrip()
k = len(string)
res = 0
point = [0 for _ in range(26)]

for w in string:
    point[ord(w) - 97] += 1

def dfs(depth, now):
    global res
    if depth == k:
        res += 1
        return

    for w in set(list(string)):
        if point[ord(w) - 97] > 0 and w != now:
            point[ord(w) - 97] -= 1
            dfs(depth + 1, w)
            point[ord(w) - 97] += 1

dfs(0, '')
print(res)