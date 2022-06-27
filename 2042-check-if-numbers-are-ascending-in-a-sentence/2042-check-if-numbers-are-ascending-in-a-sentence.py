class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr = [x for x in s.split()]
        res = []
        flag = 0
        for i in range(len(arr)):
            if(arr[i].isnumeric()):
                res.append(arr[i])

        for i in range(len(res)-1):
            if int(res[i])<int(res[i+1]):
                flag = 0
            else:
                flag = 1
                break

        if flag:
            return(False)
        else:
            return(True)
        