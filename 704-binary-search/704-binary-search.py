class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i = 0 
        j =len(nums)-1 
        while(i<=j):
            ele = i+(j-i)//2 
            if nums[ele] == target:
                return ele
            if target<nums[ele]:
                j=ele-1 
            else:
                i = ele+1
                
        return -1
        