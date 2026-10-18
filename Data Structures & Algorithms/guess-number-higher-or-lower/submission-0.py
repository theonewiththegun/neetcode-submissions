# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 0, n
        # n = 3, 1 2 3 (0 1 2)
        # lo hi = 0 2, mid = 0 + (2-0) / 2 = 1
        # hi -> 1, mid = 0 + (1-0) // 2 = 0 (== lo)
        # вроде работает
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if guess(mid) < 0: 
                hi = mid - 1
            elif guess(mid) > 0:
                lo = mid + 1
            else:
                return mid