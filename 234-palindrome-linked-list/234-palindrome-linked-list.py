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
        l = 0
        r = len(a)-1
        while r>=l:
            if a[l] == a[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True