# 트리 순회, S1, 트리
from sys import stdin

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def pre_order(node):
    print(node.data, end="")
    if node.left:
        pre_order(tree[node.left])
    if node.right:
        pre_order(tree[node.right])

def in_order(node):
    if node.left:
        in_order(tree[node.left])
    print(node.data, end="")
    if node.right:
        in_order(tree[node.right])

def post_order(node):
    if node.left:
        post_order(tree[node.left])
    if node.right:
        post_order(tree[node.right])
    print(node.data, end="")



n = int(stdin.readline())
tree = {}
for _ in range(n):
    a, b, c = stdin.readline().split()
    if b == '.':
        b = None
    if c == '.':
        c = None
    tree[a] = Node(a,b,c)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])