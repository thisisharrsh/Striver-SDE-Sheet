class Solution:
    def minSwaps(self, s: str) -> int:
        
        swap = 0
        imbalance = 0
        for i in s:
            if i == '[':
                imbalance += 1
                
            elif(imbalance):
                imbalance -= 1

            else:
                imbalance+=1
                swap+=1
        return(swap)
    
    