# 다음 순열, S3, 수학

from sys import stdin
from itertools import permutations

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

for i in range(n-1, 0, -1):
    if arr[i-1] < arr[i]: # 뒤의 수가 앞의 수 보다 크다
        for j in range(n-1, 0, -1):
            if arr[i-1] < arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:])
                print(*arr)
                exit()
print(-1)       # 만약 맨 앞의 수가 가장 큰 수고, 그 뒤가 내림차순이라면


# 이렇게 가면 메모리 초과가 난다
# res = list(permutations(arr, n))
# res.sort()
#
# for i in range(len(res)):
#     if list(res[i]) == arr:
#         if i == len(res)-1:
#             print(-1)
#         else:
#             print(*res[i+1])