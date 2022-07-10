class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=0
        j=0
        for element in pushed:
            pushed[i]=element
            while i>=0 and popped[j]==pushed[i]:
                j+=1
                i-=1
            i+=1

        if i==0:
            return True
        return False
        