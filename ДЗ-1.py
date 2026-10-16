# Вариант"В лоб"
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
#Вариант через HashMap
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       seen = {}
       for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num]=i 
