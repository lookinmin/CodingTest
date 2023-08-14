# 등수 매기기, S3, 그리디

from sys import stdin

n = int(stdin.readline())
arr = list(int(stdin.readline().rstrip()) for _ in range(n))
arr.sort()
res = 0
for i in range(1, n+1):
    res += abs(i - arr[i-1])

print(res)