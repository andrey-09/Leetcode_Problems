#Time: O(logn)
#Space: O(1)
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
    
        
        left=1
        right=n
        result=1
        #binary searhc:
        while left<=right:
            mid=(left+right)//2
            if isBadVersion(mid):
                #there are bad versions in the middle
                right=mid-1
                result=mid
            else:
                #no bad versions in the middle
                left=mid+1
        
            
            
        return result
