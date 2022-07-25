class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        nums = list(set(nums))
        low = 0 
        high = len(nums)-1 
        while(low<=high):
            mid = (low+high)//2 
            
            if nums[mid]==target:
                return True
            if nums[low]<=nums[mid]:
                if target <= nums[mid] and target>=nums[low]:
                    high = mid-1 
                else:
                    low = mid+1 
            else:
                if target>=nums[mid] and target<=nums[high]:
                    low = mid+1 
                else:
                    high = mid-1 
                    
        return False
        