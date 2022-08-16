# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,l):
        prevptr = None
        currptr = l
        nextptr = l
        
        while currptr:
            nextptr = currptr.next
            currptr.next = prevptr
            prevptr = currptr
            currptr = nextptr 
        return prevptr
            
        
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        
        lminusOne = None
        l = None
        r = None
        c = 1
        temp = head
        
        while temp:
            if c == left-1:
                lminusOne = temp
            elif c == left:
                l = temp
            elif c == right:
                r = temp.next
                temp.next = None
                break
            temp = temp.next
            c += 1
            
        newHead = self.rev(l)
        
        if lminusOne == None:
            head = newHead
        else:
            lminusOne.next = newHead
            
        l.next = r
        
        return head
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        