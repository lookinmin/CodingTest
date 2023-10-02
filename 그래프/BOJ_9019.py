# DSLR, G4, BFS

from sys import stdin
from collections import deque
# D = X2
# S = -1
# L = rotate(-1)
# R = rotate(1)

T = int(stdin.readline())



def D(num):
    tmp = num*2
    if tmp > 9999:
        tmp %= 10000
    return tmp

def S(num):
    if num == 0:
        return 9999
    else:
        return num - 1

def L(num):
    front = num%1000
    back = num//1000
    res = front*10 + back
    return res

    # 숫자->문자->숫자 : 시간초과 발생
    # tmp = str('{:0>4}'.format(num))
    # q = deque(tmp)
    # q.rotate(-1)
    #
    # val = ''
    # for i in range(len(q)):
    #     val += str(q.popleft())
    # return int(val)

def R(num):
    front = num%10
    back = num // 10
    res = front*1000 + back
    return res

def bfs(A, B):
    q = deque()
    visited = set()
    q.append((A, ""))
    visited.add(A)

    while q:
        now, oper = q.popleft()

        if now == B:
            print(oper)
            return
        tmp = D(now)
        if tmp not in visited:
            visited.add(tmp)
            q.append((tmp,oper + 'D'))

        tmp = S(now)
        if tmp not in visited:
            visited.add(tmp)
            q.append((tmp, oper + 'S'))

        tmp = L(now)
        if tmp not in visited:
            visited.add(tmp)
            q.append((tmp, oper + 'L'))

        tmp = R(now)
        if tmp not in visited:
            visited.add(tmp)
            q.append((tmp, oper + 'R'))

for _ in range(T):
    A, B = map(int, stdin.readline().split())

    bfs(A, B)
