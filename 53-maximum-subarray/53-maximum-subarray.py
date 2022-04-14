class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans=-100000
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            ans=max(ans,sum)
            if sum<0:
                sum=0
        return ans
        