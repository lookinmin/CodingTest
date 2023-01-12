# 킹, S3, 구현-시뮬레이션

from sys import stdin

king, rock, n = stdin.readline().split()
n = int(n)

def trans(a):
    if a == "A":
        return 1
    elif a == "B":
        return 2
    elif a == "C":
        return 3
    elif a == "D":
        return 4
    elif a == "E":
        return 5
    elif a == "F":
        return 6
    elif a == "G":
        return 7
    elif a == "H":
        return 8


kingR = trans(king[0])
kingC = int(king[1])
rockR = trans(rock[0])
rockC = int(rock[1])

k = [kingR, kingC]
s = [rockR, rockC]


move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

x = 0
y = 0

for i in range(n):
    m = input()
    x = k[0] + move[m][0]
    y = k[1] + move[m][1]
    if 0 < x <= 8 and 0 < y <=8:
        if x == s[0] and y == s[1]:
            sx = s[0] + move[m][0]
            sy = s[1] + move[m][1]
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [x, y]
                s = [sx, sy]
        else:
            k = [x, y]

print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')