class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashmap=set()
        for i in nums:
            hashmap.add(i)
        count = 0 
        longest_count = 0 
        for val in nums:
            if(val-1 not in hashmap):
                count = 0
                while(val in hashmap):
                    val = val+1 
                    count = count+1 
                longest_count = max(longest_count,count)
        return(longest_count)
        