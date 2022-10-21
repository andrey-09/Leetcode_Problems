# Time: O(n). recusrsive funtion: T(n)=2T(n/2)+1
# Space: O(n)- wrost case (create an array with n nodes), average case O(logn) - for having that many nodes on hold
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive solution-------------------------
        arr=[]
        self.helper(root,arr)
        return arr
    
    def helper(self, root, arr):
        
        if root:
            self.helper(root.left,arr)
            arr.append(root.val)
            self.helper(root.right,arr)
       #..............................................
      
      
