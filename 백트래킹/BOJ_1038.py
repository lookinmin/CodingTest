# 감소하는 수, G5, 완탐, 백트래킹

from sys import stdin
from itertools import combinations          # 조합 사용

n = int(stdin.readline())
nums = []

for i in range(1, 11):                          # 조합 10개 만들기
    for c in combinations(range(0, 10), i):     # 0~9사이 숫자로 조합 생성 (길이 i개) # 1 -> 10(열자리 수까지)
        c = list(c)
        c.sort(reverse=True)
        nums.append(int("".join(map(str, c))))

nums.sort()

try:
    print(nums[n])
except:
    print(-1)
