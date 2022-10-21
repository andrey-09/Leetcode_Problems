# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #stop the recursion, if there is only 1 head left or the other one is None
        if not head or not head.next: 
            return head
            

        # find the mid point in the linked list
        mid=self.getMid(head)
        
        
        #divide the list into 2 parts: 
        tmp=mid.next
        mid.next=None
        mid=tmp
        
        #divide and sort the left branch 
        left=self.sortList(head)

        #divide and sort the right branch
        right=self.sortList(mid)

        return self.merge(left, right)
    
    
    
    def getMid(self,head):
        """
        get a pointer to the middle list of the linked list
        """
        
        slow=head
        fast=head.next
        
        while (fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            #so, when we reach the right part the mid points to the middle
        return slow
    
    def merge(self, left, right):
        """
        return a pointer to the beginning of the merged sorted list 
        """
        
        head=new=ListNode()
        while (left and right): 
            
            if left.val>right.val:
                new.next=right
                right=right.next
            else:
                new.next=left
                left=left.next
            new=new.next
        
        #so, now in new, is the whole linked list! Now, we have to take care of the part that is still
        
        if left:
            new.next=left
        if right:
            new.next=right
            
        return head.next
