class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                temp = 0 
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp 
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                temp = 0 
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix)-1-j]
                matrix[i][len(matrix)-1-j] = temp 
                
        