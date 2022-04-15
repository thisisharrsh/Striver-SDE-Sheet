class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow =  fast =  get = 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                while get!= slow:
                    get = nums[get]
                    slow = nums[slow]
                return get