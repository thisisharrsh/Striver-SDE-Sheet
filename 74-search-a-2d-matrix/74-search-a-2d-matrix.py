class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        flag = False
        for i in matrix:
            low  = 0 
            high = len(i)-1 
            while(low<=high):
                mid = (low+high)//2
                if i[mid] == target:
                    flag = True
                if i[mid] < target:
                    low = mid+1 
                else:
                    high = mid-1 
        return flag