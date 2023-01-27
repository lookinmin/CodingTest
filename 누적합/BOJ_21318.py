# 피아노 체조, S1, 누적합
# N = 1 ~ 10^9
# 1<=x<=y<=N
# i의 난이도 > i+1의 난이도 -> 실수 + 1

from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
psum = [0] * n

for i in range(1, n):
    if arr[i-1] > arr[i]:
        psum[i] = psum[i-1] + 1
    else:
        psum[i] = psum[i-1]


q = int(stdin.readline())
for _ in range(q):
    x, y = map(int, stdin.readline().split())
    print(psum[y-1] - psum[x-1])
