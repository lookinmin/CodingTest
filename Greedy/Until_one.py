# 그리디 예제, 1이 될 때 까지
# N이 1이 될 때까지,
# 1. N - 1
# 2. N / K
# 를 반복하며, 2번 연산은 N이 K로 나누어 떨어질 때만 선택 가능
# 과정 수행의 최소 횟수 ?

from sys import stdin
n,k=map(int, stdin.readline().split())
cnt = 0
while n != 1:
    if n % k == 0 and k >= 2:
        n = n // k
        cnt += 1
    else:
        n = n-1
        cnt += 1

print(cnt)