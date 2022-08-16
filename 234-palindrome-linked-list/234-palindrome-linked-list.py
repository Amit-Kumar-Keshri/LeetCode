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
        c = -1
        while head:
            if head.val == a[c]:
                head = head.next
                c -= 1
            else:
                return False
            
        return True