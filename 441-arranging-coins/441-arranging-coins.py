class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        low = 0 
        high = n
        while(low<=high):
            mid = (low+high)//2 
            curr = mid*(mid+1)//2 
            if curr == n:
                return mid 
            if n<curr:
                high = mid-1
            else:
                low = mid+1 
                
        return high
        