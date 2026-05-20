# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._sort(pairs, 0, len(pairs) - 1)
    
    def _sort(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs

        m = (e + s) // 2 # 0 5 4, m = 5; 3 5
        self._sort(pairs, s, m)  # left
        self._sort(pairs, m + 1, e)  # right

        self._merge(pairs, s, m, e)
        return pairs

    def _merge(self, pairs, s, m, e):
        l = pairs[s:m+1]
        r = pairs[m+1:e+1]
        _t, _l, _r = s, 0, 0
        # print(f'pairs={[x.key for x in pairs]}, l={[x.key for x in l]}, r={[x.key for x in r]}, {s=}, {m=}, {e=}')

        while _l < len(l) and _r < len(r):
            if l[_l].key <= r[_r].key:
                pairs[_t] = l[_l]
                _l += 1
            else:
                pairs[_t] = r[_r]
                _r += 1
            _t += 1

        while _l < len(l):
            pairs[_t] = l[_l]
            _l += 1
            _t += 1

        while _r < len(r):
            pairs[_t] = r[_r]
            _r += 1
            _t += 1

