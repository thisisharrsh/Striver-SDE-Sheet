class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        i = 1 
        while (i*i <= num):
            res = i
            i = i + 1
        if res * res == num:
            return True
        else:
            return False
        