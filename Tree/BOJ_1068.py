# 트리, G5, 트리
# 주어진 트리에서 노드 하나 삭제 -> 남은 트리에서 리프노드의 개수는?
# 중간 노드를 지우면 노드와 노드 children 전부 삭제

from sys import stdin
n = int(stdin.readline())       # 노드의 개수
tree = list(map(int, stdin.readline().split()))
erase = int(stdin.readline())

def dfs(v):
    tree[v] = -2    # 해당 노드 삭제
    for i in range(n):
        if v == tree[i]:        # 지우고자 하는 노드가 어떤 자식의 부모라면
            dfs(i)              # 해당 자식 노드도 삭제

dfs(erase)
cnt = 0

for i in range(n):
    if tree[i] != -2 and i not in tree:     # 지워지지 않고, 자식이 없으면
        cnt += 1

print(cnt)