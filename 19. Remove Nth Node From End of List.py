# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reverse_head = 0
        list = []
        while head :
            list.append(head.val)
            head = head.next
        del list[-n]
        original_head = ListNode()
        dummy = original_head
        if len(list) != 0:
            for i, v in enumerate(list):
                dummy.val = v
                if i != len(list)-1:
                    dummy.next = ListNode()
                    dummy = dummy.next
            return original_head
        else:
            return original_head.next
