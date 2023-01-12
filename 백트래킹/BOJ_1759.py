# 암호 만들기, G5, 수학-백 트래킹 - 브루트포스(완탐)

from sys import stdin
from itertools import combinations

L, C = map(int, stdin.readline().split())
words = sorted(list(map(str, stdin.readline().split())))
mo = {'a', 'e', 'i', 'o', 'u'}

def make():
    res = []
    for i in list(combinations(words, L)):
        v_cnt = c_cnt = 0
        for j in i:
            if j in mo:
                v_cnt += 1
            else:
                c_cnt += 1
        if v_cnt >= 1 and c_cnt >= 2:
            res.append("".join(i))
    return res

# 문자열 조합 같음 cCl

for k in make():
    print(k)