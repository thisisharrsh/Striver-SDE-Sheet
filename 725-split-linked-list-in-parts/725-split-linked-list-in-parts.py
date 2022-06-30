# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        len = 0
        curr =head
        while curr:
            len = len+1 
            curr = curr.next
        size = len//k
        extra = len%k
        
        temp = [[]for i in range(k)]
        prev,curr = None,head
        for j in range(k):
            temp[j] = curr
            for j in range(size + (1 if extra>0 else 0)):
                prev,curr = curr , curr.next
            if prev:
                prev.next = None
            extra-=1 
                
        return temp
        