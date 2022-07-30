# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        head = dummy
        t = head
        
        while t!= None:
            p = t.next
            while p!=None and p.val == val:
                p = p.next
            t.next = p
            t = t.next
            
        return dummy.next
            
            
            
            
        
        