# Cubeditor, G3, 문자열, KMP알고리즘
# 어떤 문자열 내에서 부분 문자열이 두 번 이상 나오는 문자열을 찾는 기능

from sys import stdin

s = list(stdin.readline().rstrip())

def failure(s):
    table = [0] * len(s)
    j = 0

    for i in range(1, len(s)):
        # i(접미)와 j(접두)가 가르키는 문자가 다르다면
        # j- 1의 failure로 j는 이동
        while j > 0 and s[i] != s[j]:
            j = table[j-1]

        # i가 가르키는 문자와 j가 가르키는 문자가 같다면
        # j += 1, failure[i] += 1
        # j = 0 ~ j까지의 문자열 중 가장 길게 매칭된 부분 패턴의 길이
        if s[i] == s[j]:
            j += 1
            table[i] = j
    return table

res = 0
for i in range(len(s)):
    res = max(res, max(failure(s[i:])))

print(res)