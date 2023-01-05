# 이건 꼭 풀어야 해!, 실버3, 누적합
# 길이 n 짜리 수열 a.
# b = a를 오름차순 정렬
# L R = b(l) + ... + b(r) 가 q개
from sys import stdin

n, q = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
psum = [0 for _ in range(n+1)]
b = a.sort()
for i in range(1, n+1):
    psum[i] = psum[i-1] + a[i-1]

for i in range(q):
    l, r = map(int, stdin.readline().split())
    print(psum[r] - psum[l-1])
