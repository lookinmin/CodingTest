# 배, G5, 그리디

from sys import stdin

n = int(stdin.readline())
crain = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
boxes = list(map(int, stdin.readline().split()))

crain.sort(reverse= True)
boxes.sort(reverse= True)

if boxes[0] > crain[0]:
    print(-1)
    exit(0)
else:
    time = 0
    while boxes:
        if not boxes:
            break

        for i in crain:
            for box in boxes:
                if i >= box:
                    boxes.remove(box)
                    break
        time += 1
    print(time)


