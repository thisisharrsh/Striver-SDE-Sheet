class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        total=m+n-1
        
        left=m-1
        right=n-1
        
        while (total>=0):
            if(left>=0 and right>=0 and nums1[left]>nums2[right]):
                nums1[total]=nums1[left]
                left=left-1
                
            elif(right>=0):
                nums1[total]=nums2[right]
                right=right-1
                
            total=total-1