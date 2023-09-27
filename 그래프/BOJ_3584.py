# 가장 가까운 공통 조상, G4, DFS, Tree
# LCA

# LCA 문제해결 방법
# 1. 각 노드들의 부모노드들을 저장
# 2. 루트부터 내려오면서 비교해 같지 않은 노드가 나올때까지 반복
# 3. 처음으로 다른 노드가 나오면 해당 노드의 부모가 LCA

from sys import stdin
import sys

sys.setrecursionlimit(10**8)

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    p_list = [0 for _ in range(n+1)]        # 각 노드들의 부모노드만 필요함

    for _ in range(n-1):
        a, b = map(int, stdin.readline().split())
        p_list[b] = a       # 노드b의 부모노드는 a

    u, v = map(int, stdin.readline().split())
    u_parent = [u]      # u의 부모노드들을 찾음
    v_parent = [v]      # v의 부모노드들을 찾음

    while p_list[u]:        # u노드의 부모가 루트일때까지 찾아가며
        u_parent.append(p_list[u])  # 해당 노드들의 부모들을 모두 저장
        u = p_list[u]

    while p_list[v]:
        v_parent.append(p_list[v])
        v = p_list[v]

    u_depth = len(u_parent) - 1
    v_depth = len(v_parent) - 1     # 두 노드를 같은 depth로 맞추고 내려가면서 부모 비교

    while u_parent[u_depth] == v_parent[v_depth]:
        u_depth -= 1
        v_depth -= 1        # 부모가 같다면 하나 아래로 내려가 다시 비교

    res = v_parent[v_depth + 1]     # 마지막으로 위치한 depth의 부모가 둘이 다르기 때문에 해당 노드 하나 위의 노드에서의 부모가 답
    print(res)