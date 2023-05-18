# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_1 = []
        dummy_2 = []
        while(l1.next != None):
            dummy_1.append(l1.val)
            l1 = l1.next
        dummy_1.append(l1.val)
        while(l2.next != None):
            dummy_2.append(l2.val)
            l2 = l2.next
        dummy_2.append(l2.val)
        num1 = int("".join([str(i) for i in dummy_1[::-1]]))
        num2 = int("".join([str(i) for i in dummy_2[::-1]]))
        sum = str(num1 + num2)
        res = None
        for i in sum:
            node = ListNode(i)
            node.next = res
            res = node
        return res