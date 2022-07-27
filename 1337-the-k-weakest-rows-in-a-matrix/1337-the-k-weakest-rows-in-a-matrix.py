class Solution:
    def binarySearch(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        
        ans=-1
        
        while left<=right:
            mid = (left+right)//2
            if arr[mid]==1:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans+1
    
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=[]
        finalAns=[]
        
        for i in range(len(mat)):
            ans.append((i, self.binarySearch(mat[i])))
        
        ans = sorted(ans, key=lambda value: value[1])
        
        for i in range (0, k):
            finalAns.append(ans[i][0])
        
        return finalAns
        
        