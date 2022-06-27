class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        lefta = capacityA
        leftb = capacityB
        steps = 0

        i = 0 
        j = len(plants)-1

        while(i<j):
            if lefta>=plants[i]:
                lefta = lefta - plants[i]
                i= i+1
            else:
                lefta = capacityA
                lefta = lefta - plants[i]
                steps = steps+1
                i=i+1 

            if leftb>= plants[j]:
                leftb = leftb - plants[j]
                j = j-1
            else:
                leftb = capacityB
                leftb = leftb - plants[j]
                steps = steps+1
                j = j-1

            if i == j and lefta<plants[i] and leftb<plants[i]:
                return(steps+1)
        return(steps)