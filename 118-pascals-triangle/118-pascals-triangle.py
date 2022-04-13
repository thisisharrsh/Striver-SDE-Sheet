class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle = [[1], [1,1]]
        if numRows == 1:
            return([[1]])

        for i in range(1, numRows-1):
            current = [1]
            for k in range(len(triangle[i])-1):
                current.append(triangle[i][k] + triangle[i][k+1])
            current.append(1)
            triangle.append(current)

        return(triangle)
