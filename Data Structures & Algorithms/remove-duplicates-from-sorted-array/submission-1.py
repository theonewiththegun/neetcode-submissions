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
            
            nums[j] = None
            j += 1

        vacant = None
        curr = 0
        k = 0
        while curr < len(nums): # O(n)
            if nums[curr] is not None:
                k += 1
                if vacant is not None:
                    nums[vacant] = nums[curr]
                    vacant += 1
            else:
                if vacant is None:
                    vacant = curr
            
            curr += 1

        return k
        