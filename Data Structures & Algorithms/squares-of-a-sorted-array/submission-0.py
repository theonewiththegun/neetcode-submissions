class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                out.append(nums[l] ** 2)
                l += 1
            else:
                out.append(nums[r] ** 2)
                r -= 1
        
        return out[::-1]