class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = []
        count = nums.count(target)
        if count > 0:
            index = nums.index(target)
            second = index + count - 1
            output.append(index)
            output.append(second)
            return output
        else:
            return [-1,-1]
        