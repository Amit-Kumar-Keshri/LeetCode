# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if(not head or not head.next or k==0):
            return head
        
        temp= head
        n = 1
        while temp.next:
            temp = temp.next
            n += 1
        temp.next = head
    
        newHead = None
        k = n -(k%n)
        c = 1
        while c != k:
            head = head.next
            c += 1
        #print(head.val) 
        newHead = head.next
        head.next = None
        return newHead
        
            
            
            
            
            
        