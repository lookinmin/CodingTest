# 트리와 쿼리, g5, 트리
# unweighted, undirected
# 걍 그래프 아니냐 시발
# 트리에서 마지막 입력받는 정점을 루트로 하는 서브트리의 정점의 수 출력
# dfs


from sys import stdin
import sys
sys.setrecursionlimit(10**9)

n, r, q = map(int, stdin.readline().split())
tree = [[] for _ in range(n+1)]
count = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def countPoint(v):
    count[v] = 1
    for i in tree[v]:
        if count[i] == 0:       # 방문하지 않은 노드라면
            countPoint(i)       # dfs() 수행
            count[v] += count[i]    # 서브트리의 수 +

countPoint(r)

for _ in range(q):
    m = int(stdin.readline().rstrip())
    print(count[m])
