# 정보 상인 호석, G5, 우선순위큐
from sys import stdin
import heapq
from collections import defaultdict
n = int(stdin.readline())
dic = defaultdict(list)
k = 0
for _ in range(n):
    arr = list(map(str, stdin.readline().split()))

    if arr[0] == '1':
        for num in arr[3:]:
            heapq.heappush(dic[arr[1]], -int(num))

    else:
        if arr[1] not in dic.keys():
            continue

        if len(dic[arr[1]]) <= int(arr[2]):
            for _ in range(len(dic[arr[1]])):
                k += -heapq.heappop(dic[arr[1]])
        else:
            for _ in range(int(arr[2])):
                k += -heapq.heappop(dic[arr[1]])

print(k)
