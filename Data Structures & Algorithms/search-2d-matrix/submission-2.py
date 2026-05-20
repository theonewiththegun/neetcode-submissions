class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ub = self._upper_bound(matrix, target)
        if ub > 0:
            return self._simple_binary_search(matrix[ub - 1], target)
        else:
            return False



    def _upper_bound(self, matrix: List[List[int]], target: int) -> int:
        # t = 12, [0, 9, 10, 12]
        # do not discard mid if it becomes hi
        lo, hi = 0, len(matrix) - 1
        while lo < hi:
            mid = lo + ((hi - lo) // 2) # to avoid overflow
            print(lo, mid, hi)
            if matrix[mid][0] > target:
                hi = mid
            else:
                lo = mid + 1
        return hi if matrix[hi][0] > target else hi + 1

    def _simple_binary_search(self, array: List[int], target: int) -> bool:
        lo, hi = 0, len(array) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if array[mid] > target:
                hi = mid - 1
            elif array[mid] < target:
                lo = mid + 1
            else:
                return True
        return False

        