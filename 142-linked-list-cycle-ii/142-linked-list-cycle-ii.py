# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        
        while (fast and slow and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
            
            if slow==fast:
                entry=head
                
                while entry!=slow:
                    entry, slow = entry.next, slow.next
                return entry
            
        return None
        