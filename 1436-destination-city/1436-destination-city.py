class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        result = ""
        d = {}
        for j in paths:
            for i in j:
                if i in d:
                    d[i]+=1 
                else:
                    d[i]=1
        ans = [i for i in d.keys() if d[i] == 1]
        for i in paths:
            if i[1] in ans:
                result = i[1]
        return(result)
        