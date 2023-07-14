# 아카라카, S2, 문자열 - 재귀

import sys
sys.setrecursionlimit(10**6)
s = list(input().rstrip())

def pelin(s):     # s의 길이가 짝수, 홀수 일 때를 구분해야 함
    k = len(s)
    if k == 1:
        return True

    if s == s[::-1]:
        if k % 2 == 0:
            if pelin(s[:k//2]) and pelin(s[k//2:]):
                return True
        else:
            if pelin(s[:k // 2]) and pelin(s[k // 2 + 1:]):
                return True
    else:
        return False


if pelin(s):
    print("AKARAKA")
else:
    print("IPSELENTI")