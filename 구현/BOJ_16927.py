# 배열돌리기2, G5, 구현

from sys import stdin

n, m, r = map(int,stdin.readline().split())
arr = [[] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, stdin.readline().split()))

def rotate(i, j, n, m):
    top = arr[i][j]
    left = arr[n-1][j]
    bottom = arr[n-1][m-1]
    right = arr[i][m-1]

    for x in range(n-1, i, -1):
        arr[x][j] = arr[x-1][j]         # 한칸 내리기

    for x in range(i, n-1):
        arr[x][m-1] = arr[x+1][m-1]     # 한칸 올리기

    for y in range(j, m-1):
        arr[i][y] = arr[i][y+1]         # 한칸 왼쪽으로

    for y in range(m-1, j, -1):
        arr[n-1][y] = arr[n-1][y-1]     # 한칸 오른쪽으로

    arr[i+1][j] = top
    arr[n-1][j+1] = left
    arr[n-2][m-1] = bottom
    arr[i][m-2] = right

height = min(n, m) // 2             # 몇 겹인지
cycle = (n-1) * 2 + (m-1) * 2       # 둘레 (4x4)의 경우, 제일 겉면의 값 수는 12개

for i in range(height):
    for _ in range(r % cycle):      # 회전횟수 압축
        rotate(i, i, n-i,m-i)
    cycle -= 8                      # 한겹의 차이는 8칸차이

for x in arr:
    print(*x, sep=' ')