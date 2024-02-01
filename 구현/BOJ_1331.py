# 나이트 투어, S4

x_wi = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6}
arr = []
for i in range(36):
    arr.append(input().rstrip())

visited = []
prev = [x_wi[arr[0][0]], int(arr[0][1])]
visited.append(prev)
for move in arr[1:]:
    x, y = move[0], int(move[1])
    cx = x_wi[x]
    if [cx, y] in visited:
        print("Invalid")
        exit()

    if abs(prev[0] - cx) == 1 and abs(prev[1] - y) == 2:
        prev = [cx, y]
        visited.append(prev)
        continue
    elif abs(prev[0] - cx) == 2 and abs(prev[1] - y) == 1:
        prev = [cx, y]
        visited.append(prev)
        continue
    else:
        print("Invalid")
        exit()

if abs(visited[-1][0] - visited[0][0]) + abs(visited[-1][1] - visited[0][1]) != 3:
    print("Invalid")
    exit()

print("Valid")