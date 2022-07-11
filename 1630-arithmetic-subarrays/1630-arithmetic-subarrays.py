class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(nums,l,r):
            arr = nums[l:r+1]
            arr.sort()
            for i in range(len(arr)-1):
                if arr[i+1]-arr[i]!= arr[1]-arr[0]:
                    return(False)
            return True
        
        res = []

        for i in range(len(l)):
            new_l = l[i]
            new_r = r[i]
            z = check(nums,new_l,new_r)
            res.append(z)

        return(res)
        