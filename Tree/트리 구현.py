# 노드 만들기
#         A(val)
#        /      \
#   B(left)     C(right)
class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


# 이진트리 만들기
class BinaryTree:
    # 초기값 head는 None
    def __init__(self):
        self.head = Node(None)

        self.preorder_list=[]
        self.inorder_list=[]
        self.postorder_list=[]

    # 값 추가하기 head가 없을 경우
    def add(self, item):
        if self.head.val is None:
            self.head.val = item

        # head가 있으면 왼쪽배치 or 오른쪽배치
        else:
            self.__add_node(self.head, item)

    # head가 있는 경우
    def __add_node(self, cur, item):
        print('부모:', cur.val, '자식:', item)
        # head 값이 크면 왼쪽으로
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        # head 값이 작으면 오른쪽으로
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)

    # 찾기!!
    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        print(cur.val, item)
        if cur.val == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.__search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.__search_node(cur.right, item)
                else:
                    return False

    # 전위순회
    def preorder_traverse(self):
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self, cur):
        self.preorder_list.append(cur.val)
        print(cur.val)
        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)

    # 중위순회
    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)

        self.inorder_list.append(cur.val)
        print(cur.val)

        if cur.right is not None:
            self.__inorder(cur.right)

    # 후위순회
    def postorder_traverse(self):
        if self.head is not None:
            self.__postorder(self.head)

    def __postorder(self, cur):
        if cur.left is not None:
            self.__postorder(cur.left)

        if cur.right is not None:
            self.__postorder(cur.right)

        self.postorder_list.append(cur.val)
        print(cur.val)


lst = [50, 30, 24, 5, 28, 45, 98, 52, 60]
bt = BinaryTree()
for num in lst:
    bt.add(num)


print(bt.search(60))
# 전우
bt.preorder_traverse()
print(bt.preorder_list)
# 중위
bt.inorder_traverse()
print(bt.inorder_list)
# 후위
bt.postorder_traverse()
print(bt.postorder_list)

# 출처: https://www.youtube.com/watch?v=0CqDdXOr6Kk