class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        flag = False
        for i in matrix:
            for j in i:
                if j ==  target:
                    flag = True

        return (flag)
        