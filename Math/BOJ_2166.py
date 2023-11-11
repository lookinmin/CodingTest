# 다각형의 면적, G5, 기하학

from sys import stdin

n = int(stdin.readline())
arr = []
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    arr.append((x,y))

res = 0
for i in range(1, n-1):
    res += ((((arr[i][0]-arr[0][0])*(arr[i+1][1]-arr[0][1])) - ((arr[i+1][0] - arr[0][0])*(arr[i][1] - arr[0][1]))) / 2)

# 점의 위치가 주어졌을때 다각형의 넓이 구하는 공식
# S = 시그마(i=2 ~ n-1) ((xi-x1)*(yi+1-y1) - (xi+1-x1)*(yi-y1)) / 2
# S는 넓이 이므로 절댓값
print("{:.1f}".format(abs(res)))