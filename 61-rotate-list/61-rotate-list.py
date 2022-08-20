# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if(not head or not head.next or k==0):
            return head
        
        t = head
        n = 0
        while t:
            t = t.next
            n += 1
            
        temp = head
        c = 1
        k =(k%n)
        
        if(k == 0):
            return head;
        swap_node = None
        while temp:
            if c == (n-k):
                swap_node = temp.next
                temp.next = None
                break
            temp = temp.next
            c+=1
        
        t1 = swap_node
        while t1.next:
            t1 = t1.next
        t1.next = head
        return swap_node
            
            
            
            
        