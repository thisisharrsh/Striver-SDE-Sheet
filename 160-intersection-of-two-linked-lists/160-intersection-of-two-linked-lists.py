# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA 
        temp2 = headB 
        count1 = 0 
        count2 = 0
        diff = 0
        while(temp1!=None):
            count1+=1
            temp1=temp1.next 
        while(temp2!=None):
            count2+=1 
            temp2 = temp2.next
            
        diff = count1 - count2
        
        
        if diff<0:
            count = 0
            while(count < abs(diff)):
                count+=1 
                headB = headB.next 
        else:
            count = 0
            while(count < abs(diff)):
                count+=1 
                headA = headA.next
                
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next