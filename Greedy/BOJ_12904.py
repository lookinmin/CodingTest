# A와B, G5, 그리디, 구현, 문자열
# 1. 문자열 뒤에 A 추가
# 2. 문자열 뒤집고 뒤에 B 추가

# T -> S 가는게 맞는듯

from sys import stdin
S = list(stdin.readline().strip())
T = list(stdin.readline().strip())
switch = False

while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
    if S==T:
        switch = True
        break
if switch:
    print(1)
else:
    print(0)
