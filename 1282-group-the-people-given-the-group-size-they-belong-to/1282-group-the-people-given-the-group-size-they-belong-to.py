class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res=[]
        d={}
        for i in range(len(groupSizes)):
            if groupSizes[i] in d:
                d[groupSizes[i]].append(i)
            else:
                d[groupSizes[i]]=[i]

            if(len(d[groupSizes[i]])==groupSizes[i]):
                res.append(d[groupSizes[i]])
                d[groupSizes[i]]=[]
        return(res)