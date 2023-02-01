# 트럭, S1, 구현
# n개의 트럭, w대의 트럭만 가능

from sys import stdin
n,w,l = map(int, stdin.readline().split())
arr = list(map(int,stdin.readline().split()))

bridge = [0] * w
time = 0

while bridge:
    time += 1
    bridge.pop(0)
    if arr:
        if sum(bridge) + arr[0] <= l:
            bridge.append(arr.pop(0))
        else:
            bridge.append(0)

print(time)