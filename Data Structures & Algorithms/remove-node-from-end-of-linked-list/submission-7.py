# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next
        temp = head
        for i in range(n):
            temp = temp.next

        dummy = ListNode()
        curr = dummy
        curr.next = head

        while temp:
            curr = curr.next
            temp = temp.next

        curr.next = curr.next.next

        return dummy.next

        

        


        