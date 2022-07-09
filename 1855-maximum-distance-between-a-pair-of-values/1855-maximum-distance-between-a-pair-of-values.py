class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        dis = 0

        while(i<n) and (j<m):
            if nums1[i]<=nums2[j]:
                dis = max(dis,(j-i))
            else:
                i+=1 
            j+=1 

        return(dis)
        