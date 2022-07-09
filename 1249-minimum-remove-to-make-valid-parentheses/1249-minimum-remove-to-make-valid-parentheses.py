class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        remove = []

        for index,element in enumerate(s):
            if element == "(":
                stack.append(index)
            elif element == ")":
                if len(stack)!=0:
                    stack.pop()
                else:
                    remove.append(index)

        to_ignore = set(stack+remove)
        string = ""
        for i in range(len(s)):
            if i in to_ignore:
                pass 
            else:
                string+=s[i]

        return(string)
        