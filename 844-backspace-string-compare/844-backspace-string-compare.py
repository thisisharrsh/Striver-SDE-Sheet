class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack_s = []
        stack_t = []

        for i in s:
            if i == '#' and len(stack_s)==0:
                pass
            elif i == '#':
                stack_s.pop()
            else:
                stack_s.append(i)


        for j in t:
            if j == '#' and len(stack_t)==0:
                pass
            elif j == '#':
                stack_t.pop()
            else:
                stack_t.append(j)

        re_s = "".join(stack_t)
        re_t = "".join(stack_s)

        if re_t == re_s:
            return(True)
        else:
            return(False)
        