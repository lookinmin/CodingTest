# ⚾, G4, 구현-완탐
# 1번 선수 -> 무조건 4번타자
# 삼성 A형 기출문제

from sys import stdin
from itertools import permutations

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split()))for _ in range(n)]

max_score = 0

def game(line_ups):
    hit = 0
    score = 0
    for i in arr:   # 각 이닝 당
        out = 0
        b1,b2,b3 = 0,0,0        # 1루, 2루, 3루
        while out < 3:
            if i[line_ups[hit]] == 0:
                out += 1
            elif i[line_ups[hit]] == 1:     # 1루타
                score += b3                 # 현재 3루에 있는 사람 들어옴(+1)
                b1,b2,b3 = 1, b1, b2        # 1루에 +1명, 2,3루로 각 이동
            elif i[line_ups[hit]] == 2:     # 2루타
                score += (b2+b3)            # 현재 2,3루에 있는 사람 들어옴(+2)
                b1, b2,b3 = 0, 1, b1        # 2루타 쳤으니까 1루는 무조건 비고, 나머지 이동
            elif i[line_ups[hit]] == 3:
                score += (b2 + b3 + b1)
                b1,b2,b3 = 0,0,1
            else:                           # 홈런
                score += (1 + b1 + b2 + b3) # 나 + 지금 있는 사람 모두
                b1,b2,b3 = 0,0,0            # 베이스 리셋
            hit = (hit + 1) % 9
    return score

for i in permutations(range(1,9), 8):
    line_ups = list(i[:3]) + [0] + list(i[3:])
    max_score = max(max_score, game(line_ups))

print(max_score)