class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = len(arr1)
        for i in range(len(arr1)):
            l=0
            r=len(arr2)-1
            while l <= r:
                mid = (l+r)//2
                if abs(arr1[i] - arr2[mid]) <= d:
                    count = count - 1
                    break
                elif arr1[i] <= arr2[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return count
