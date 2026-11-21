# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        [1, 2, 3, 4, 5, 6]
        [1, 2]
        if not head.next:
            return head.next
        temp = head
        for i in range(n):
            temp = temp.next

        dummy = head
        curr = head
        prev = None
        [1, 2]
        while temp:
            prev = curr
            curr = curr.next
            temp = temp.next

        if not prev:
            return curr.next
        else:
            prev.next = curr.next
            return head

        

        


        