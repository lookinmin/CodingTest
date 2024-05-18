# 서강근육맨, S3
from sys import stdin
# 운동을 하면 근손실이 남?
n = int(stdin.readline())
arr = sorted(list(map(int, stdin.readline().split())))

res = 0
if n % 2 == 0: # 짝수
    left = arr[: n//2]
    right = arr[n//2 : ][::-1]
    
    for i in range(n//2):
        res = max(res, left[i] + right[i])
else:
    k = arr[-1]
    arr.pop()
    m = n - 1
    left = arr[: m // 2]
    right = arr[m // 2 : ][::-1]
    res = max(res, k)
    
    for i in range(n//2):
        res = max(res, left[i] + right[i])

print(res)
