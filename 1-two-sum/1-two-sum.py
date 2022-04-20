class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = []
        for i,n in enumerate(nums):
            differ = target-n
            if differ in d:
                return [i,d[differ]]
            d[n] = i
            
            
       