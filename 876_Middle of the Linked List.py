# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        find the middle nod of a linked list
        """
        #solve with 2 pointers:
        
        slow=fast=head
        
        while (fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            
        return slow
