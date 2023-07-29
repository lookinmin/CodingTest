# 캐슬 디펜스, G3, 구현
# 삼성 기출 -> combination 직접 구현
import copy
from sys import stdin

n, m, d = map(int, stdin.readline().split())

graph = [[] for _ in range(n)]
arrow = [i for i in range(m)]       # 궁수가 위치할 수 있는 경우의 수(N+1)행
res = 0

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

def combinations(arr, r):           # combination 함수, import해서 사용할 수 있으나 삼성기출이라 만들어서 함
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]      # 제너레이터 생성, 결과값을 그때 그때 리턴함
        else:
            for next in combinations(arr[i+1 : ], r - 1):
                yield [arr[i]] + next


def moveDown():         # 그래프 한칸 밑으로 내리는 함수
    for i in range(n-2, -1, -1):    # 가지고 내려오고, 한칸 올라가서 탐색
        tmp[i+1] = tmp[i]
    tmp[0] = [0 for _ in range(m)]

def clear():
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 1:
                return False
    return True

def attack(comb):
    # 거리가 D 이하인 적 중 가장 가까운 적 공격

    attack_list = []                                    # 공격해야할 대상 삽입 리스트
    cnt = 0                                             # 공격으로 없앨 수 있는 적 수

    for arrow in comb:
        pos = []                                        # 공격가능 대상 삽입할 리스트
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 1:
                    now_d = abs(i-n) + abs(j-arrow)         # 궁수랑 적의 거리
                    if d >= now_d:                  # 사거리 내에 적 있으면
                        pos.append((now_d, i, j))   # 공격가능 대상에 추가

        pos.sort(key=lambda x : (x[0], x[2]))   # 거리 기준, 왼쪽(j) 기준
        if pos:
            attack_list.append(pos[0])      # 제거할 적 삽입

    for enemy in attack_list:
        _, i, j = enemy
        if tmp[i][j] == 1:
            tmp[i][j] = 0
            cnt += 1
    return cnt


for comb in combinations(arrow, 3):     # 궁수는 m개의 칸 중 3개의 칸에 위치 가능 -> 조합으로 확인
    tmp = copy.deepcopy(graph)
    cnt = 0
    while not clear():
        cnt += attack(comb)
        moveDown()

    res = max(res, cnt)

print(res)

