class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        i = 0
        while i < len(nums)-1 :
            if nums[i+1] == nums[i] :
                if count < 1:
                    count += 1
                else:
                    nums.pop(i+1)
                    i -= 1
            else:
                count = 0
            i += 1
        