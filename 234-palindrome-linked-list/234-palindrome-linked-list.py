# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head 
        stack = []
        length = 0
        
        while(slow!=None):
            stack.append(slow.val)
            length = length+1
            slow = slow.next
            
            
        while(fast!=None):
            if fast.val!=stack.pop(length-1):
                return False
            else:
                fast = fast.next 
                length = length-1
                
        return True