class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        dictt={}
        for i in range(len(logs)):
            if dictt.get(logs[i][0],-1)==-1:
                dictt[logs[i][0]]=set([logs[i][1]])
            else:
                dictt[logs[i][0]].add(logs[i][1])
                
        ans = [0]*(k+1)
        for i in dictt:
            ans[(len(dictt[i]))]+=1 
        return ans[1::]