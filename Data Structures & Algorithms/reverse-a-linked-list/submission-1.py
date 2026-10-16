# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #eg [5,4,3,2,1] -> [1,2,3,4,5]
        #2 sol, recursive, iterative(do this one)
        #we need a temp variable
        #p = c, c = t
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev


        #O(n) time, O(1) space



        
        
        