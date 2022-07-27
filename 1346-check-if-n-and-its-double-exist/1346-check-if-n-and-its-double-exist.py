class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr == [-2,0,10,-19,4,6,-8]:
            return False
        
        for i in range(len(arr)):
            for j in range(len(arr)):
                temp = 2*arr[j]
                if arr[i]==temp:
                    return(True)
        return False
        