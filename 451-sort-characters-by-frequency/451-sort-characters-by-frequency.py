class Solution:
    def frequencySort(self, s: str) -> str:
        d={} 

        for i in s:
            if i not in d:
                d[i]=1 
            else:
                d[i]+=1

        d = sorted(list(d.items()),key=lambda x:x[1],reverse=True)

        ans = ''
        for i in d:
            ans+= i[0]*i[1]

        return(ans)
