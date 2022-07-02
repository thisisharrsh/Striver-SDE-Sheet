class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        nums=[]
        if num/3==num//3:
            x = int(num/3)
            nums.append(x-1)
            nums.append(x)
            nums.append(x+1)

        return(nums)