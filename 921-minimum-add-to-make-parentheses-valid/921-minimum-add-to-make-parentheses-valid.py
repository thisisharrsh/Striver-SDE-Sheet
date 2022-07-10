class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        count=0
        count1 = 0 
        for i in s:
            if i=='(':
                count1+=1
            else:
                count1+=-1
                
            if count1 == -1:
                count1+=1 
                count+=1
        return(count1+count)
        