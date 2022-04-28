# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lengthoflist(self,head):
        length = 0
        temp = head
        while(temp!=None):
            temp = temp.next
            length = length+1
        return length
    
    def reverse(self,head,k,length):
        if length<k:
            return head
        count,nex,prev,curr = 0,None,None,head
        while(count<k and curr!=None):
            nex = curr.next
            curr.next = prev
            prev = curr 
            curr = nex
            count+=1
        if nex!=None:
            head.next = self.reverse(nex,k,length-k)
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.lengthoflist(head)
        return self.reverse(head,k,length)
            
        