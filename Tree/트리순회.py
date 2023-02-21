class Node:             # 노드를 클래스로 선언해야함
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node):        # 전위 순회
    print(node.data, end=" ")       # 일단 나부터
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

def in_order(node):         # 중위 순회
    if node.left_node:              # 일단 왼쪽자식부터
        in_order(tree[node.left_node])
    print(node.data, end=" ")
    if node.right_node:
        in_order(tree[node.right_node])

def post_order(node):       # 후위 순회
    if node.left_node:              # 왼 -> 우 -> 나
        post_order(tree[node.left_node])
    if node.right_node:
        post_order(tree[node.right_node])
    print(node.data, end=" ")

n = int(input())        # 트리의 크기(노드의 개수)
tree = {}               # 딕셔너리를 통한 트리 구현

for i in range(n):
    data, left, right = input().split()
    if left == "None":
        left = None
    if right == "None":
        right = None
    tree[data] = Node(data,left,right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])