# 참외밭, S2, 구현
# 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
from sys import stdin
k = int(stdin.readline().rstrip())

height = []
width = []
total = []

for i in range(6):
    b, l = map(int, stdin.readline().split())
    if b == 1 or b == 2:
        width.append(l)
        total.append(l)
    else:
        height.append(l)
        total.append(l)

tmp = max(width) * max(height)

maxW = total.index((max(width)))
maxH = total.index((max(height)))

# 전체 이동에서 세로 최대값의 다음값에서 세로 최대값 이전의 가로값을 빼준다 = 작은 사각형의 가로
smallW = abs(total[maxH-1] - total[(maxH-5 if maxH == 5 else maxH + 1)])
smallH = abs(total[maxW-1] - total[(maxW-5 if maxW == 5 else maxW + 1)])

res = tmp - smallW*smallH
print(res * k)