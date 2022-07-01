# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head,head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        while(slow):
            temp = slow.next
            slow.next = prev 
            prev = slow
            slow = temp
            
        
        max_sum = 0
        sum1 = 0
        
        left = head
        right = prev
        
        while(right):
            sum1 = left.val + right.val
            max_sum = max(max_sum,sum1)
            left = left.next
            right = right.next
            
        return(max_sum)
        
        