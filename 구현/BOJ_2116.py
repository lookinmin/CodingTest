# 주사위 쌓기, G5, 구현-완탐
# 한 옆면의 숫자의 합이 최대

from sys import stdin
n = int(stdin.readline())       # 주사위의 갯수
dice = [list(map(int, input().split())) for _ in range(n)]
rotate = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}       # 각자 마주보는 면의 값을 딕셔너리로 저장
res = []

for i in range(6):
    max_dice = []
    st_dice = [1,2,3,4,5,6]         # 기준이 되는 주사위 (가장 밑에 있는것)

    bottom_side = dice[0][i]        # 가장 밑의 주사위의 밑바닥의 값
    up_side = dice[0][rotate[i]]    # 맞은편에 위치한 윗면의 값

    st_dice.remove(bottom_side)      # 주사위의 바닥과
    st_dice.remove(up_side)          # 주사위의 윗면을 주사위의 값에서 제거

    max_dice.append(max(st_dice))    # 남은 값들 중 가장 큰값을 저장

    for j in range(1, n):
        next_dice = [1,2,3,4,5,6]
        bottom_side = up_side       # 가장 밑의 것의 윗면과 아랫면이 일치

        up_side_idx = rotate[dice[j].index(up_side)]
        up_side = dice[j][up_side_idx]

        next_dice.remove(bottom_side)
        next_dice.remove(up_side)

        max_dice.append(max(next_dice))     # 남은 값들 중 가장 큰 값 저장

    res.append(sum(max_dice))

print(max(res))

