from sys import stdin

# row 하나 확인 or col 하나 확인

board = []
for i in range(3):
    board.append(list(map(int, stdin.readline().split())))

# row 먼저

def func(a, b, c):
    value = a + b + c - min(a, b, c) - max(a, b, c)
    return abs(value - a) + abs(value - b) + abs(value - c)

res = int(1e9)

for i in range(3):
    a, b, c = board[i]
    if a == b == c:
        print(0)
        exit()
    else:
        tmp = func(a, b, c)
        res = min(res, tmp)

for i in range(3):
    arr = []
    for j in range(3):
        arr.append(board[j][i])
    if arr[0] == arr[1] == arr[2]:
        print(0)
        exit()
    else:
        tmp = func(arr[0], arr[1], arr[2])
        res = min(res, tmp)

print(res)