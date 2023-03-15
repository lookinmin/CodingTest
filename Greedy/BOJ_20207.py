# 달력, S1, 그리디 - 구현

from sys import stdin
n = int(stdin.readline())

calendar = [0] * 367
todo = []
for _ in range(n):
    s, e = map(int, stdin.readline().split())
    calendar[s] += 1        # 시작부분 인덱스 + 1
    calendar[e+1] -= 1      # 종료부분 인덱스 - 1

width, height = 0, 0        # 가로 세로 초기화
res = 0

for i in range(1, 367):
    calendar[i] += calendar[i-1]
    if calendar[i] == 0:            # 연속되는 배열이 종료되는 부분
        res += width * height       # 현재 만들어진 직사각형의 넓이를 더해주고
        width, height = 0, 0        # 가로세로 초기화
    else:
        width += 1                  # 한칸 넘어갈 때 마다 가로길이 + 1
        height = max(height, calendar[i])

print(res)