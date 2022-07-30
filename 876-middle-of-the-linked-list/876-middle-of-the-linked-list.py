# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        
        while head != None:
            head = head.next
            count += 1
            
            
        m = count//2
        
        x=0
        while x!=m:
            temp = temp.next
            x+=1
            
        return temp
        
        
        