# 나무 자르기, S2
from sys import stdin
n = int(stdin.readline())
trees = list(map(int, stdin.readline().split()))
grows = list(map(int, stdin.readline().split()))

res = 0
arr = []

for i in range(n):
    arr.append([trees[i], grows[i]])

arr.sort(key = lambda x : x[1])
# 성장속도 기준 정렬

for i in range(n):
    res += (arr[i][0] + arr[i][1] * i)

print(res)