class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = []
        res = []
        stack.append(arr[-1])

        res.append(-1)

        for i in range(len(arr)-2,-1,-1):
            if arr[i]>stack[-1]:
                res.append(stack[-1])
                stack.append(arr[i])
            else:
                res.append(stack[-1])

        res.reverse()
        return(res)

        