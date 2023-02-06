# 파일 합치기3, G4, 그리디-우선순위 큐
from sys import stdin
import heapq

T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    res = 0
    q = []

    for i in arr:
        heapq.heappush(q, i)
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        res += a+b
        heapq.heappush(q, a+b)
    print(res)

    # 시간 초과 -> 우선순위 큐 사용으로 순회
    # while True:
    #     arr = sorted(arr)
    #     tmp = arr[0] + arr[1]
    #     arr.pop(0)
    #     arr.pop(0)
    #     arr.append(tmp)
    #     res += tmp
    #
    #     if len(arr) == 2:
    #         break
    # res += sum(arr)
    # print(res)