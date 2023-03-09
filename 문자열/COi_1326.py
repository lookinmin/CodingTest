# 회문 판별기
from sys import stdin
s = str(stdin.readline().rstrip())

if s == s[::-1]:
    print("YES")
else:
    print("NO")