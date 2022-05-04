class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        j = -1 
        count = 0
        ans = 0
        for i in range(len(nums)):
            if(nums[i]==0):
                count=count+1 
            while(count>k):
                j+=1 
                if(nums[j]==0):
                    count-=1 
            length = i-j
            if(length>ans):
                ans = length

        return(ans)
        