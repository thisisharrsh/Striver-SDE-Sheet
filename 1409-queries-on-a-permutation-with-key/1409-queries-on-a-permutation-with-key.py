class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        perm = []
        res=[]
        for m in range(1,m+1):
            perm.append(m)

        for i in range(len(queries)):
            temp = queries[i]
            for j in range(len(perm)):
                if temp == perm[j]:
                    res.append(j)
                    perm.insert(0,perm.pop(j))
        return(res)
        