# 시간표 짜기, S2
from sys import stdin
n = int(stdin.readline())
lecture = []

for _ in range(n):
    lecture.append(list(map(int, stdin.readline().split()))[1:])

m = int(stdin.readline())

for _ in range(m):
    now = list(map(int, stdin.readline().split()))[1:]
    # 총 수업 가능 시간 1 ~ 50
    bit = [0] * 51
    for num in now:
        bit[num] = 1

    cnt = 0
    for lec in lecture:
        flag = True
        for num in lec:
            if bit[num] == 0:
                flag = False
                break
        if flag:
            cnt += 1
        else:
            continue

    print(cnt)


