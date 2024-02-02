from sys import stdin

h, w = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

res = 0

for i in range(1, w-1):
    leftH = max(arr[:i])
    rightH = max(arr[i+1:])
    H = min(leftH, rightH)

    if arr[i] < H:
        res += H - arr[i]

print(res)