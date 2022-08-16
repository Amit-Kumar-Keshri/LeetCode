# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def rev(self,temp):
#         p, c , n = None, temp , temp 
        
#         while c:
#             n = c.next
#             c.next = p 
#             p = c
#             c = n
#         return p
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        #new = self.rev(temp)
        a = []
        
        while temp:
            a.append(temp.val)
            temp = temp.next
        
        while head:
            if head.val == a[-1]:
                head = head.next
                a.pop()
            else:
                return False
            
        return True