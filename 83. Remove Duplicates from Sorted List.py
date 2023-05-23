# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # empty_list = []
        # while head:
        #     if head.val not in empty_list:
        #         empty_list.append(head.val)
        #     head = head.next
        # list_node = ListNode()
        # temp = list_node
        # for i in empty_list:
        #     temp.next = ListNode(i)
        #     temp = temp.next
        # return list_node.next

        if not head:
            return None
        
        temp = head
        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
