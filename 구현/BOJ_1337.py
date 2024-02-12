# S4, 올바른 배열
from sys import stdin
N = int(stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(stdin.readline()))

arr.sort()

tmp = []

for i in range(N):
    cnt = 0
    for j in range(arr[i], arr[i] + 5):
        if j not in arr:
            cnt += 1
    tmp.append(cnt)

print(min(tmp))