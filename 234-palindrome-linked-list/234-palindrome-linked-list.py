# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        list1 = []
        while(curr!=None):
            list1.append(curr.val)
            curr = curr.next
        i=0
        j=len(list1)-1
        while(i<j):
            if list1[i]!=list1[j]:
                return False
            i=i+1
            j=j-1
        return True
    