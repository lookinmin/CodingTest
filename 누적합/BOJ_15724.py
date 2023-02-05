# 주지수, S1, 누적합
from sys import stdin

n,m=map(int, stdin.readline().split())

arr = [[0]*m for _ in range(n)]
psum = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    arr[i]= list(map(int,stdin.readline().split()))

k = int(stdin.readline())

for i in range(n+1):
    for j in range(m+1):
        psum[i][j] = arr[i-1][j-1]+psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]

for _ in range(k):
    x1,y1, x2,y2 = map(int,stdin.readline().split())
    print(psum[x2][y2] - psum[x1-1][y2] - psum[x2][y1-1] + psum[x1-1][y1-1])