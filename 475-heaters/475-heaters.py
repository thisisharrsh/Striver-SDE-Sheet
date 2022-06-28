class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters.append(math.inf)
        radius = 0
        i = 0
        
        for house in houses:
            while abs(house - heaters[i + 1]) <= abs(house - heaters[i]):
                i += 1
            radius = max(radius, abs(house - heaters[i]))
        
        return radius