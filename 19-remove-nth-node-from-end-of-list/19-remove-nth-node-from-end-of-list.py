# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        z = ListNode(0, head)
        p = z
        q=head 
        while(n):
            q = q.next
            n = n-1
            
        while(q):
            q = q.next 
            p = p.next 
            
        p.next = p.next.next 
        return z.next
        