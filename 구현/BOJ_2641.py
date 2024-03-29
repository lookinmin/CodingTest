# 다각형 그리기, S2
from sys import stdin
from collections import deque

n = int(stdin.readline())
standard = list(map(int, stdin.readline().split()))

rev_std = []
for num in standard:
    if num == 1:
        rev_std.append(3)
    elif num == 2:
        rev_std.append(4)
    elif num == 3:
        rev_std.append(1)
    else:
        rev_std.append(2)

m = int(stdin.readline())
arr = []
for _ in range(m):
    arr.append(list(map(int, stdin.readline().split())))

res = 0
ans = []
for i in range(m):
    q = deque(standard)
    rev_q = deque(rev_std[::-1])
    k = 2*n

    while k > 0:
        if deque(arr[i]) == q or deque(arr[i]) == rev_q:
            res += 1
            ans.append(arr[i])
            break
        else:
            q.rotate(1)
            rev_q.rotate(1)

        k -= 1

print(res)
for arr in ans:
    print(*arr)