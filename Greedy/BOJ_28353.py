from sys import stdin

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort(reverse=True)

res = 0

while 1:
    if len(arr) == 1 or len(arr) == 0:
        break
    
    if arr[0] >= k:
        arr.pop(0)
        continue
    
    if arr[0] + arr[-1] <= k:
        res += 1
        arr.pop(0)
        arr.pop()
        continue
    else:
        arr.pop(0)
        continue
    
print(res)

# 9 7 6 5 4 3