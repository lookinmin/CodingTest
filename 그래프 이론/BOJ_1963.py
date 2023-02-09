# 소수 경로, G4, 그래프, 에라토스테네스의 체
from sys import stdin
from collections import deque

def findPrime():
    # 에라토스테네스의 체(제곱근 범위까지 조사)
    for i in range(2, 100):
        # 소수인 상태에서 소수의 배수를 체크해줘야 함
        if prime[i] == True:
            # 소수의 배수 체크
            for j in range(2*i, 10000, i):
                prime[j] = False

def bfs(a,b):
    q = deque()
    q.append([a, 0])
    visited = [0 for _ in range(10000)]
    visited[a] = 1
    while q:
        now, cnt = q.popleft()
        strNow = str(now)
        if now == b:
            return cnt
        for i in range(4):
            for j in range(10):
                tmp = int(strNow[:i] + str(j) + strNow[i+1:])
                if visited[tmp] == 0 and prime[tmp] and tmp > 999:
                    visited[tmp] = 1
                    q.append([tmp, cnt + 1])

T = int(stdin.readline())

prime = [True for _ in range(10000)]
findPrime()

for _ in range(T):
    a, b = map(int, stdin.readline().split())
    res = bfs(a,b)
    print(res if res != None else "Impossible")