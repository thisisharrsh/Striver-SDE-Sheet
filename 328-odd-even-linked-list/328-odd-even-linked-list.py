# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        odd = head
        even = head.next
        dummy = head.next

        while odd.next and even.next:
            odd.next = odd.next.next
            if odd.next:
                odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = dummy
        return head