class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = max(arr)
        temp=[]
        for i in range(1,n+k+1):
            if i not in arr:
                temp.append(i)
        return(temp[k-1]) 
        