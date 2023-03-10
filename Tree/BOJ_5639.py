# 이진 검색 트리, G5, 트리
# BST

from sys import stdin
import sys
sys.setrecursionlimit(10**6)
nums = []

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.head = Node(None)
        self.postorder_list = []

    def add(self, data):
        if self.head.data is None:
            self.head.data = data
        else:
            self.__add_node(self.head, data)

    def __add_node(self, cur, data):
        if cur.data >= data:
            if cur.left is not None:
                self.__add_node(cur.left, data)
            else:
                cur.left = Node(data)
        else:
            if cur.right is not None:
                self.__add_node(cur.right, data)
            else:
                cur.right = Node(data)

    def postorder_traverse(self):
        if self.head is not None:
            self.__postorder(self.head)

    def __postorder(self,cur):
        if cur.left is not None:
            self.__postorder(cur.left)
        if cur.right is not None:
            self.__postorder(cur.right)
        self.postorder_list.append(cur.data)
        print(cur.data)

while 1:
    try:
        n = int(stdin.readline())
        nums.append(n)
    except:
        break

bt = BST()
for i in nums:
    bt.add(i)

bt.postorder_traverse()

#-----------------------------------리스트로 구현-------------------------------------
from sys import stdin
import sys
sys.setrecursionlimit(10**6)
nums = []

while 1:
    try:
        n = int(stdin.readline())
        nums.append(n)
    except:
        break

def postorder(start, end):
    if start > end:
        return
    mid = end + 1       # root가 가장 큰 값일 경우

    for i in range(start + 1, end + 1):
        if nums[start] < nums[i]:       # 시작값 보다 크다면
            mid = i
            break

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(nums[start])

postorder(0, len(nums)-1)