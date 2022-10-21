#Medium_
# Time:  O(n^2) - worst case: we compare them to each one
# Space: O(1) - we reordered the nodes of the list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Idea: create a circular list
        head_new=ListNode()
        curr=head
        
        #iterate through the given list and find an appropriate place 
        while curr:
            
            #to iterate throught:
            tail_new=head_new

            #get to the point where the value is less or equal to the value we have:
            #because our linked list is already sorted!
            while tail_new.next and tail_new.next.val <= curr.val:
                tail_new=tail_new.next
            
            # now we are in the middle of a new linked list in the right position, so we should save the 
            # the part that comes after tail_new.next
        
            curr_next=curr.next 
            curr.next=tail_new.next
            tail_new.next=curr
            
            
            #next step
            curr=curr_next
        
        return head_new.next
