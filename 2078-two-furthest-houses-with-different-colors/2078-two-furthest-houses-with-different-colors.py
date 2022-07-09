class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        i=0
        j=len(colors)-1 

        dis1 = 0
        dis2 = 0
        while(i<j):
            if colors[i]!=colors[j]:
                dis1 = max(dis1,(abs(i-j)))
                break
            j=j-1

        i=0
        j=len(colors)-1 

        while(i<j):
            if colors[i]!=colors[j]:
                dis2 = max(dis2,(abs(i-j)))
                break
            i=i+1

        return(max(dis1,dis2))
        