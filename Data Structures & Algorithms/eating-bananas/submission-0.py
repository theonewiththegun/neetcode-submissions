from math import ceil

class Solution:
    def works(self, piles: List[int], speed: int, cap: int):
        turns = 0
        for p in piles: # O(n)
            turns += ceil(p / speed)
        if turns <= cap:
            return True
        return False


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles) # this is k (speed), min always 1, max - the biggest pile size, to finish eating in len(piles), cannot go faster than that
        out = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.works(piles, mid, h):
                out = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return out
            
