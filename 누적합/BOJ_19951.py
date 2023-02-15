# 태상이의 훈련소 생활, S1, 누적합
# 카카오 블라인드 1차 6번 <- 2차원 배열로 확장시킨 문제
# 구간합을 통한 갱신 -> 아이디어 알아놓기

from sys import stdin
n,m = map(int,stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
tmp = [0] * (n+1)
for _ in range(m):
    a, b, k = map(int, stdin.readline().split())
    tmp[a-1] += k
    tmp[b] -= k
    # print(*tmp)

psum = [0] * (n+1)
psum[0] = tmp[0]

for i in range(1, n+1):
    psum[i] = psum[i-1] + tmp[i]

# print(*psum)

for i in range(n):
    arr[i] += psum[i]
print(*arr)