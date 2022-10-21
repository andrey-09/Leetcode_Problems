class Solution:
    def mySqrt(self, x: int) -> int:

        #and the try a binary search
        # Time: O(logn) 
        #Space O(1)
        
        left, right=0, x
        
        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid

        # left > right
        return right
        
        
