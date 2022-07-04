class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums+nums
        m = len(nums)
        n = len(nums2)
        nge = [0]*n 
        stack = []

        for i in range(n-1,-1,-1):
            while(stack and stack[-1]<=nums2[i%n]):
                stack.pop()

            if not stack:
                nge[i] = -1
            else:
                nge[i] = stack[-1]
            stack.append(nums2[i])

        return(nge[:m])
        