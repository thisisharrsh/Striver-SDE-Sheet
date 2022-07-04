class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        for i in nums1:
            index_i = nums2.index(i)
            while index_i < len(nums2):
                if index_i<len(nums2)-1 and nums2[index_i+1] > i:
                    stack.append(nums2[index_i+1])
                    break
                index_i+=1
            else:
                stack.append(-1)
        return stack
        