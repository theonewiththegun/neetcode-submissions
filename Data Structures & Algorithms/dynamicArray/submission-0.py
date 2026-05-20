class DynamicArray:
    
    def __init__(self, capacity: int):
        self._arr = [None for _ in range(capacity)]
        self._ptr = -1
        self._cap = capacity

    def get(self, i: int) -> int:
        if 0 <= i < self._cap:
            return self._arr[i]
        else:
            raise ValueError('OOB')

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self._cap:
            self._arr[i] = n
        else:
            raise ValueError('OOB')

    def pushback(self, n: int) -> None:
        self._ptr += 1
        if self._ptr >= self._cap:
            self.resize()
        self._arr[self._ptr] = n

    def popback(self) -> int:
        if self._ptr < 0:
            raise ValueError('OOB')
        self._ptr -= 1
        return self._arr[self._ptr + 1]

    def resize(self) -> None:
        new = [None for _ in range(self._cap * 2)]
        for i in range(self._cap):
            new[i] = self._arr[i]
        self._arr = new
        self._cap *= 2

    def getSize(self) -> int:
        return self._ptr + 1
    
    def getCapacity(self) -> int:
        return self._cap
