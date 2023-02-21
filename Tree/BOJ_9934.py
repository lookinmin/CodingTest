# 완전 이진 트리, S1, 트리-recursion
# 중위 순회, in_order
from sys import stdin

# 가장 가운데 수 = tree의 루트 -> 분할정복
def sol(start, end, depth):
    if start == end:
        ans[depth].append(tree[start])
        return
    mid = (start + end) // 2        # 분할정복을 통해 parent 노드를 depth에 맞춰 in
    ans[depth].append(tree[mid])
    sol(start, mid-1, depth + 1)
    sol(mid+1, end, depth + 1)

k = int(stdin.readline())
tree = list(map(int, stdin.readline().split()))
ans = [[] for _ in range(k)]

sol(0, len(tree) - 1, 0)
for i in ans:
    print(*i)

