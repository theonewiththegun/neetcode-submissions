
class Solution: # O(n^2) time, O(1) space
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        i = 0
        j = 1
        while j < len(nums): # O(n)
            if nums[i] != nums[j]:
                i = j
                j += 1
                continue
            
            del nums[j] # O(n)

        return len(nums)