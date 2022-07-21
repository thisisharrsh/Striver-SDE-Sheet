class Solution:
    def mySqrt(self, x: int) -> int:
        l= 0 
        r = x
        while(l<=r):
            mid = (l+r)//2 
            val = mid*mid
            if val == x:
                return mid 
            elif(val<x):
                l = mid+1
            else:
                r= mid-1 
                
        return l-1