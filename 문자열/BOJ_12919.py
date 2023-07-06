# A와B 2, G5, 문자열

from sys import stdin

S = list(stdin.readline().rstrip())
T = list(stdin.readline().rstrip())

# 1. 문자열 뒤에 A 추가
# 2. B 추가하고 reverse

# 거꾸로 생각하기 = t -> s
def make(t):
    if S == t:
        print(1)
        exit(0)
    if len(t) == 0 :
        return 0
    if t[-1] == 'A':    # t의 마지막이 A임
        make(t[:-1])    # 마지막꺼 빼고 dfs
    if t[0] == 'B':     # t의 시작이 B임
        make(t[1:][::-1])   # 처음꺼 빼고 돌려서 dfs

make(T)

print(0)



