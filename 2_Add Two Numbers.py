#Time: O(max(m,n))
#Space: O(max(m,n))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        head=tail=ListNode()
        more=0
        while (l1 or l2 or more!=0):
            
            l1va=l1.val if l1 else 0
            l2va=l2.val if l2 else 0
            
            sum1=(l1va+l2va)
            tail.next=ListNode( (sum1+more) %10)
            more=(sum1+more)//10
            
            #next step
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            tail=tail.next
    
        
        
        
        return head.next
            
            
            
            
            
