class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        low = 0
        high = 1000 
        
        while(low<=high):
            mid = (low+high)//2 
            
            count = 0 
            for i in nums:
                if i>=mid:
                    count = count+1 
            if count == mid:
                return count 
            if count<mid:
                high = mid-1 
            if count>mid:
                low = mid+1 
                
        return -1
                    
        