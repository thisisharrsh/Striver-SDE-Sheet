# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while(slow and fast and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
            
            if slow==fast:
                return True
        return False
            
        