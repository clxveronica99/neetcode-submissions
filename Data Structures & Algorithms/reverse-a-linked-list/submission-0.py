# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev, curr = head, head.next
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head.next = None
        return prev