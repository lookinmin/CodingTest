# 배열 복원하기, S3, 구현

from sys import stdin
h, w, x, y = map(int, stdin.readline().split())
arr= []
for i in range(h+x):
    arr.append(list(map(int, stdin.readline().split())))

for i in range(h):
    for j in range(w):
        arr[x+i][y+j] = arr[x+i][y+j] - arr[i][j]

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=" ")
    print()