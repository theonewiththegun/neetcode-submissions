class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None

        p, c = None, 0
        k = 0
        while c < len(nums):
            if nums[c] is not None:
                k += 1
                if p is not None:
                    nums[p] = nums[c]
                    p += 1
            else:
                if p is None:
                    p = c

            c += 1
        
        return k

        
        