# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

# 7 3 2 5 6 4

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quick_sort_helper(pairs, 0, len(pairs) - 1)
        return pairs

    def _quick_sort_helper(self, pairs: List[Pair], s: int, e: int):
        if e - s < 1:
            return

        pivot = e  # this number will be used to split the array
        ptr = s  # current pointer, this number is currently analysed

        # this is the pointer that holds the spot for the pivot,
        # we swap lower-than-pivot numbers with it, then increment;
        # by the time ptr reaches the pivot, we have the first number
        # larger than pivot under the holder
        holder = s 

        while ptr < pivot:
            if pairs[ptr].key < pairs[pivot].key:
                pairs[ptr], pairs[holder] = pairs[holder], pairs[ptr]
                holder += 1
            ptr += 1
        
        pairs[pivot], pairs[holder] = pairs[holder], pairs[pivot]

        self._quick_sort_helper(pairs, s, holder - 1)
        self._quick_sort_helper(pairs, holder + 1, e)


        