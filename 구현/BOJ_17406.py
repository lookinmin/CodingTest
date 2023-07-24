# 배열 돌리기 4, G4, 구현

from sys import stdin
from itertools import permutations
from copy import deepcopy


n, m, k = map(int, stdin.readline().split())
arr = [[] for _ in range(n)]
rcs = []
for i in range(n):
    arr[i] = list(map(int, stdin.readline().split()))

for _ in range(k):
    rcs.append(list(map(int, stdin.readline().split())))

res = int(1e9)

def find_min(arr):
    global res
    for row in arr:
        res = min(res, sum(row))

    return res


for p in permutations(rcs, k):   # 배열 돌리는 순서가 임의로 정해짐 -> permutation
    copy_arr = deepcopy(arr)
    for r, c, s in p:
        r -= 1
        c -= 1

        for i in range(s, 0, -1):       # 테두리 하나씩 들어가기
            tmp = copy_arr[r-i][c+i]    # 오른족 위 값 저장      # 슬라이싱으로 값 회전시키기
            copy_arr[r-i][c-i+1:c+i+1] = copy_arr[r-i][c-i:c+i]   # -> 오른쪽으로 한칸 이동
            for row in range(r-i, r+i):
                copy_arr[row][c-i] = copy_arr[row + 1][c-i]       # ↑
            copy_arr[r+i][c-i:c+i] = copy_arr[r+i][c-i+1:c+i+1]     # <- 왼쪽으로 한칸이동
            for row in range(r+i, r-i, -1):
                copy_arr[row][c+i] = copy_arr[row-1][c+i]         # ↓

            copy_arr[r-i+1][c+i]=tmp        # 오른쪽 위 값 하나 밑으로 내리기

    res = find_min(copy_arr)

print(res)
