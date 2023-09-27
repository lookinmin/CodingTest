# 단절점, 단절선, S1, 그래프 - 트리

from sys import stdin
# 중요! => 트리는 사이클이 없는 그래프 이므로 모든 간선은 단절선이 된다.
# 트리에서 root와 leaf는 단절점이 아니고, 나머지는 모두 단절점이다.

n = int(stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(stdin.readline())
for _ in range(q):
    t, k = map(int, stdin.readline().split())
    if t == 1:
        if len(tree[k]) < 2:            # 나한테 연결된 노드가 0, 1개 = 단절점 아님
            print("no")
        else:
            print("yes")
    else:
        print("yes")