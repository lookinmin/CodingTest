# 걷다보니 신천역 삼, S2, 수학

from sys import stdin
from itertools import combinations
import sys
sys.setrecursionlimit(1000000)

N = int(stdin.readline())
# 0,1,2 만 가지고 N자리 3의 배수 만들기
# N = 1이면 X
# N = 2면, 12, 21 2개 왜? 더해서 3의 배수가 되어야 함
res = 0
def make_num(n, sum):
    global res
    for i in range(3):
        if n==0 and i==0:       # 가장 큰 자리 수가 0인거 방지
            continue
        if n==N:
            if sum%3==0:
                res += 1
                return res
        else:
            make_num(n+1, int(str(sum+i)))

make_num(0,0)
print(res)