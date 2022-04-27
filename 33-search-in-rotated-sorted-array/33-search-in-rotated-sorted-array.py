class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        idx = 0
        for i in range(len(nums)):
            if nums[i] == target:
                idx = i
                return idx 
            
        return -1