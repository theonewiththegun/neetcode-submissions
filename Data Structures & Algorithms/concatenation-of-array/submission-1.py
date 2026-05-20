class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [_ for _ in range(n * 2)]
        for i in range(n):
            out[i] = nums[i]
            out[n + i] = nums[i]

        return out