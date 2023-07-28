# 두 용액, G5, 이분탐색

from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

arr.sort()
start = 0
end = n-1

res = abs(arr[start] + arr[end])
final = [arr[start], arr[end]]


while start < end:
    lv = arr[start]
    rv = arr[end]

    sum_v = lv + rv

    if abs(sum_v) < res:
        res = abs(sum_v)
        final = [lv, rv]
        if res == 0:
            break
    if sum_v < 0:
        start += 1
    else:
        end -= 1

print(*final)