# 전구와 스위치, G5, 그리디

from sys import stdin

n = int(stdin.readline())
bulb = list(map(int, stdin.readline().rstrip()))
goal = list(map(int, stdin.readline().rstrip()))

def press(A, B):
    copyA = A[:]
    count = 0
    for i in range(1, n):
        if copyA[i-1] == B[i-1]:        # 현재 누르려는 스위치의 직전 전구의 상태 일치
            continue                    # 스위치를 누르지 않음

        count += 1

        for j in range(i-1, i+2):       # 다르다면 스위치 누름
            if j < n:
                copyA[j] = 1 - copyA[j]
    if copyA == B:
        return count
    else:
        return 1e9


res = press(bulb, goal)
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]

res = min(res, press(bulb, goal) + 1)

if res != 1e9:
    print(res)
else:
    print(-1)