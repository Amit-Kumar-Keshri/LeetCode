# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        c = 0
        while temp:
            c += 1
            temp = temp.next
        
        if c==n:
            return head.next
            
        a = head
        k = 1
        while k!=c-n:
            k+=1
            a = a.next
        
        a.next = a.next.next
        return head
         