from typing import TypeVar

T = TypeVar('T')

class RingBuffer:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError('capacity must be greater than 0')
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head: int = 0 # next write location
        self.tail: int = 0 # next read location
        self.size: int = 0

    def append(self, item: T) -> None:
        self.buffer[self.head] = item
        if self.is_full:
            self.tail = (self.tail + 1) % self.capacity
        else:
            self.size += 1
        self.head = (self.head + 1) % self.capacity

    def pop(self) -> T:
        if self.is_empty:
            raise IndexError('Pop from an empty ring buffer') 
        item: T = self.buffer[self.tail]
        self.buffer[self.tail] = None
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1
        return item
        
    @property
    def is_full(self) -> bool:
        return self.size == self.capacity

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def __str__(self) -> str:
        if self.is_empty:
            return '[]'
        items: list[T] = []
        for i in range(self.size):
            idx = (self.tail + i) % self.capacity
            items.append(self.buffer[idx])
        return f'RingBuffer({items})'
