# n단 논법, S1
from sys import stdin
from collections import defaultdict
from collections import deque
n = int(stdin.readline())
graph = defaultdict(list)
for _ in range(n):
    arr = list(map(str, stdin.readline().split()))
    graph[arr[0]].append(arr[2])

m = int(stdin.readline())

def bfs(start, end):
    q = deque(start)
    
    while q:
        x = q.popleft()
        
        if x == end:
            return True
        for node in graph[x]:
            q.append(node)
    
    return False

for _ in range(m):
    arr = list(map(str, stdin.readline().split()))
    if bfs(arr[0], arr[2]):
        print("T")
    else:
        print('F')