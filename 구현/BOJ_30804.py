# S2, 과일 탕후루
from sys import stdin
from collections import defaultdict
n = int(input())
arr = list(map(int, stdin.readline().split()))
hash = defaultdict(int)
    
left = 0
res = 0

for right in range(n):
    hash[arr[right]] += 1
    
    while len(hash) > 2:        # 현재 종류가 3개 이상
        hash[arr[left]] -= 1
        if hash[arr[left]] == 0:
            del hash[arr[left]]
        left += 1
    
    res = max(res, right - left + 1)

print(res)