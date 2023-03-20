# 회문은 회문이 아니야!!, G5, 문자열

from sys import stdin
import math
s = list(stdin.readline().rstrip())

k = len(s)

if s == s[0] * k:       # 한 글자만 계속 반복되는 경우
    print(-1)
elif s[:k//2][::-1] == s[math.ceil(k/2):]:      # 절반만 확인하기
    print(k-1)
else:
    print(k)


# 투포인터로 확인하기-------------------------------------------------

def check(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return 0
        start += 1
        end -= 1
    return 1

if check(s, 0, k-1) == 0:       # 회문이 아님
    print(k)
elif check(s, 0, k-2) == 0:     # 최대 길이에서 하나 뺀게 회문이 아님
    print(k-1)
else:
    print(-1)