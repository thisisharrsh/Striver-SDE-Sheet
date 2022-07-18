class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            res = res | nums[i]
        return res
        