# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''

        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        res = list(str(int(num1) + int(num2)))
        # print(res) : ['8', '0', '7']
        
        answer = ListNode(res[0], None)
        # 첫 idx를 끝 노드로

        for i in range(1, len(res)):
            tmp = ListNode(res[i], answer)
            answer = tmp
        
        
        return answer
