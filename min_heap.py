class MinHeap:
    def __init__(self) -> None:
        self.length: int = 0
        self.data: list = []

    def insert(self, value: int) -> None:
        self.data.append(value)
        self._heapify_up(self.length)
        self.length += 1

    def pop(self) -> int | None:
        if self.length == 0:
            return None
        out = self.data[0]
        if self.length == 1:
            self.data = []
            self.length -= 1
            return out
        self.length -= 1
        self.data[0] = self.data.pop(self.length)
        self._heapify_down(0)
        return out

    def _heapify_down(self, idx: int) -> None:
        l_idx: int = self._left_child(idx)
        r_idx: int = self._right_child(idx)
        if l_idx >= self.length:
            return
        min_idx: int = l_idx
        if r_idx < self.length and self.data[r_idx] < self.data[l_idx]:
            min_idx = r_idx

        if self.data[idx] > self.data[min_idx]:
            self.data[idx], self.data[min_idx] = (
                self.data[min_idx],
                self.data[idx],
            )
            self._heapify_down(min_idx)

    def _heapify_up(self, idx: int) -> None:
        if idx == 0:
            return None
        parent: int = self._parent(idx)
        parent_value: int = self.data[parent]
        value: int = self.data[idx]
        if parent_value > value:
            self.data[parent], self.data[idx] = value, parent_value
            self._heapify_up(parent)

    def _parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def _left_child(self, idx: int) -> int:
        return (idx * 2) + 1

    def _right_child(self, idx: int) -> int:
        return (idx * 2) + 2
