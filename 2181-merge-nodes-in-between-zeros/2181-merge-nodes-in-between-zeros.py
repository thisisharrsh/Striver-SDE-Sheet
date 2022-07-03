# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=head
        node=head.next
        curr_sum=0
        while(node.next):
            curr_sum+=node.val
            
            if(node.next.val==0):
                node.val=curr_sum
                curr.next=node
                curr=curr.next
                curr_sum=0
                
            prev=node
            node=node.next
            
        prev.next=None
        return head.next
        