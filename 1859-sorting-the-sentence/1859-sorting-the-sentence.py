class Solution:
    def sortSentence(self, s: str) -> str:
        arr = [x for x in s.split()]
        num = 1
        res = []
        req = ""
        while arr:
            for i in arr:
                if(int(i[-1])==num):
                    res.append(i)
                    num = num+1 
                    arr.remove(i)

        for i in res:
            req = req + ' '+ i[:-1]

        return(req.strip())
        