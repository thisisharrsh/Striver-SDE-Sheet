# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        hashset = set()
        while(headA!=None):
            hashset.add(headA)
            headA = headA.next
        while(headB!=None):
            if(headB in hashset):
                return headB
            headB = headB.next
            
        return None
        