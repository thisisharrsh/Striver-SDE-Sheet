class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        len1 = len(temperatures)
        ans = [0]*len1
        stack = []
        
        for day,temp in enumerate(temperatures):
            while(stack and temperatures[stack[-1]]< temp):
                prev = stack.pop()
                ans[prev] = day - prev 
            stack.append(day)
            
        return ans
        