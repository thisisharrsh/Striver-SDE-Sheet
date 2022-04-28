# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow=head
        fast=head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while(curr!=None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr =temp
        while(prev!=None):
            if prev.val!=head.val:
                return False
            head = head.next
            prev=prev.next
        return True
        