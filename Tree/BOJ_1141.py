# 접두사, S2, 트리
from sys import stdin

n = int(stdin.readline())
arr = []

for _ in range(n):
    arr.append(stdin.readline().rstrip())

arr.sort(key=len)
res = 0

for i in range(n):
    flag = 0
    for j in range(i+1, n):
        if arr[i] == arr[j][0:len(arr[i])]:
            flag = 1
            break
    if not flag:
        res += 1

print(res)