from sys import stdin

k = int(stdin.readline())
view = []
for i in range(6):
    dir, length = map(int, stdin.readline().split())
    view.append([dir, length])

# 1 ->
# 2 <-
# 3 south
# 4 north
maxW = 0
maxH = 0
minW = int(1e9)
for dir, length in view:
    if dir == 1 or dir == 2:
        maxW = max(maxW, length)
    elif dir == 3 or dir == 4:
        maxH = max(maxH, length)
total = maxW * maxH
minH = int(1e9)
minW = int(1e9)
for i in range(6):
    if (view[i][0] == 3 or view[i][0] == 4) and view[i][1] == maxH:
        if i == 5:
            minW = maxW - min(view[0][1], view[i - 1][1])
        elif i == 0:
            minW = maxW - min(view[-1][1], view[i + 1][1])
        else:
            minW = maxW - min(view[i + 1][1], view[i - 1][1])
    if (view[i][0] == 1 or view[i][0] == 2) and view[i][1] == maxW:
        if i == 5:
            minH = maxH - min(view[0][1], view[i - 1][1])
        elif i == 0:
            minH = maxH - min(view[-1][1], view[i + 1][1])
        else:
            minH = maxH - min(view[i + 1][1], view[i - 1][1])

print((total - (minH * minW)) * k)


