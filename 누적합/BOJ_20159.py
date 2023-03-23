# 동작 그만. 밑장 빼기냐?, G5, 누적합 prefix sum

from sys import stdin
from collections import deque

n = int(stdin.readline())
card = deque(list(map(int, stdin.readline().split())))
cnt = 0
res = 0
while card:
    tmp = card[0]
    if tmp < card[-1] and cnt == 0:
        tmp = card[-1]
        cnt += 1
    res += tmp
    card.popleft()
    card.popleft()
print(res)
# 밑장을 중간에 뺀 순간, 홀수와 짝수번째 카드가 들어가는 경우가 바뀜
#------------------------ 상대의 차례에서 카드가 바뀌는 경우를 생각 못함----------------

N = int(input())
arr = list(map(int, input().split()))

even_psum = [0] * (N//2)        # 짝수 누적합
odd_psum = [0] * (N//2)         # 홀수 누적합

even_psum[0] = arr[0]
odd_psum[-1] = arr[-1]

for i in range(1, N//2):
    even_psum[i] = arr[i*2] + even_psum[i-1]        # 짝수 누적합 계산
    odd_psum[-i-1] = arr[i*-2-1] + odd_psum[-i]     # 홀수 누적합 계산

res = 0

for i in range(len(even_psum)):
    if not i == len(even_psum) - 1:
        res = max(res, even_psum[i] + odd_psum[i+1])        # 밑장을 내가
    res = max(res, even_psum[i] + odd_psum[i] - arr[-1])    # 밑장을 상대에게

res = max(res, odd_psum[0], even_psum[-1])
print(res)
