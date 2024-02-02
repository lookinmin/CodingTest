import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

prev = int(1e9)
res = 0
for i in range(1, n):
    tmp = arr[i] - arr[i-1]

    if tmp < prev:
        res = 1
        prev = tmp
        continue
    elif tmp == prev:
        res += 1
        continue
    elif tmp > prev:
        continue
print(res)