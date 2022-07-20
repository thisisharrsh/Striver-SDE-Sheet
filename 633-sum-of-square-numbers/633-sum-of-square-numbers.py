class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0 
        r = int(math.sqrt(c))
        while(l<=r):
            a_sq = l*l 
            b_sq = r*r
            if (a_sq+b_sq == c):
                return True 
            elif(a_sq+b_sq<c):
                l = l+1
            elif(a_sq+b_sq>c): 
                r =r-1 
        return False