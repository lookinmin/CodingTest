# 문제 추천 시스템 version1, g4
from sys import stdin
import heapq

n = int(stdin.readline())
tasks = []
maxHeap, minHeap = [], []
dic = {}
for _ in range(n):
    p, l = map(int, stdin.readline().split())
    heapq.heappush(minHeap, [l, p])
    heapq.heappush(maxHeap, [-l, -p])
    dic[p] = True

m = int(stdin.readline())
for _ in range(m):
    order = stdin.readline().split()
    if order[0] == "add":
        P, L = int(order[1]), int(order[2])
        while not dic[-maxHeap[0][1]]:
            heapq.heappop(maxHeap)

        while not dic[minHeap[0][1]]:
            heapq.heappop(minHeap)
        dic[P] = True
        heapq.heappush(minHeap, [L, P])
        heapq.heappush(maxHeap, [-L, -P])


    elif order[0] == 'solved':
        P = int(order[1])
        dic[P] = False

    else:
        x = order[1]
        if x == '1':
            # 가장 어려운거
            while not dic[-maxHeap[0][1]]:
                heapq.heappop(maxHeap)
            print(-maxHeap[0][1])
        else:
            # 가장 쉬운거
            while not dic[minHeap[0][1]]:
                heapq.heappop(minHeap)
            print(minHeap[0][1])