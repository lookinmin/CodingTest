# CCW, G5, 기하학

from sys import stdin

x1, y1 = map(int, stdin.readline().split())
x2, y2 = map(int, stdin.readline().split())
x3, y3 = map(int, stdin.readline().split())

tmp = x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3

if tmp > 0:
    print(1)
elif tmp < 0:
    print(-1)
else:
    print(0)

# 신발끈 공식을 이용
# (x2-x1)(y3-y1) - (y2-y1)(x3-x1)