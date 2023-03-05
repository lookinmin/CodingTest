# 부동산 다툼, S1, 트리

from sys import stdin

N, Q = map(int,stdin.readline().split())

duck = []
for _ in range(Q):
    duck.append(int(stdin.readline().rstrip()))

tree = set()

def visit(a):       # 오리가 원하는 땅 기준으로 루트까지 거슬러 올라가기
    res = 0
    b = a
    while b > 0:
        if b in tree:
            res = b
        b //= 2     # 부모는 자식의 절반값

    if res == 0:                # 갈 수 있음 -> 도착
        tree.add(a)             # i 번째 오리가 a 땅 점유
    print(res)

for i in duck:
    visit(i)


