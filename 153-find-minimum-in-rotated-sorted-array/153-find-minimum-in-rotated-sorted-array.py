class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0 
        high = len(nums)-1 
        while(low<=high):
            mid  = (low+high)//2 
            
            if nums[high] ==  nums[mid]:
                return nums[mid]
            
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[high]>nums[mid]:
                high = mid-1 
            else:
                low = mid+1
        