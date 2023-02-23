# 소트, G5, 그리디-정렬
# 교환을 S번
from sys import stdin

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
s = int(stdin.readline())

for i in range(n):
    j = len(arr)
    while 1:
        if i == arr.index(max(arr[i : j])):
            break
        else:
            if arr.index(max(arr[i:j])) - i <= s:
                max_idx = arr.index(max(arr[i : j]))
                s -= max_idx - i
                for k in range(max_idx-1, i-1,-1):
                    arr[k], arr[k+1] = arr[k+1],arr[k]
            else:
                j -= 1

print(*arr)
