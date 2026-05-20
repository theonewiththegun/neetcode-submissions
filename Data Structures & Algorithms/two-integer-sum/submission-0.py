class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, n in enumerate(nums):
            if n in complements:
                return [complements[n], i]
            
            if target - n not in complements:
                complements[target - n] = i