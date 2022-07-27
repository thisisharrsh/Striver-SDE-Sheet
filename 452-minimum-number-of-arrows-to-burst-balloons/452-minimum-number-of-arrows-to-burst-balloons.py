class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0 
        points.sort()
        
        curr_end= points[0][1]
        arrow = 1 
        for i in points[1:]:
            if i[0]<=curr_end:
                curr_end = min(curr_end,i[1])
                
            else:
                arrow+=1 
                curr_end = i[1]
                
        return arrow