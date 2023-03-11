# 탑, G5, 스택
# 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능
# 모든 탑에서는 주어진 탑 순서의 반대 방향(왼쪽 방향)으로 동시에 레이저 신호를 발사
# 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지

from sys import stdin
n = int(stdin.readline())
arr = list(map(int ,stdin.readline().split()))
stack = []
res = [0] * n

# 오른쪽으로 이동하면서 이전 탑의 높이가 현재 탑의 높이 보다 클때만 필요
for i in range(n):
    tmp = arr[i]

    while stack and arr[stack[-1]] < tmp:       # 더 작음
        stack.pop()         # 필요 없으니 버림
    if stack:
        res[i] = stack[-1] + 1

    stack.append(i)

print(*res)