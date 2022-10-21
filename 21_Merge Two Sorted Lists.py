# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        merge two sorted linked lists list1 and list 2.
        Merge the two lists in a one sorted list
        mxn
        
        Time Complexity: O(min(m,n))
        Space: O(n+m) 
        """
        
        head=tail=ListNode()
        
        #two equal parts of two lists
        while (list1 and list2):
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        
        #if sth is still in the list
        if list1:
            tail.next=list1
        if list2:
            tail.next=list2
    
        return head.next
        
        
