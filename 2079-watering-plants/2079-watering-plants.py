class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0 
        left_water = capacity
        for i in range(len(plants)):
            if left_water>=plants[i]:
                steps+=1 
                left_water -=plants[i]
            else:
                left_water = capacity
                left_water-= plants[i]
                steps = steps + (2*i)+1 
        return(steps)
        