# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # n = 0
        # temp = head
        # while temp:
        #     temp = temp.next
        #     n +=1
        # n = n-1    
        ans = 0

        while head:
            ans = (2*ans)+head.val
            head = head.next
            
        return ans