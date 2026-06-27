from __future__ import annotations
from dataclasses import dataclass
from typing import TypeVar

V = TypeVar('V')
K = TypeVar('K')

# an LRU (least recently used) cache is a combination of a hashmap and a
# doubly linked list.  It evicts elements that have been used the least
# recently once a predefined length has been reached.  It also moves elements
# to the front of the list once the have been accessed.

@dataclass(eq = False)
class Node:
    prev: Node
    next: Node
    value: V


class LRU:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.head: Node | None
        self.tail: Node | None
        self.head = self.tail = None
        self.length: int = 0
        self._lookup: dict[K, V] = {}
        self._reverse_lookup: dict[V, K] = {}

    def update(self, key: K, value: V) -> None:
        #check the cache for existence
        # use get
        node: Node = self._lookup.get(key, None)
        # if it doesn't then we insert
        #   - check capacity and evict if we are at capacity
        if not node:
            node = Node(None, None, value)
            self.length += 1
            self._prepend(node)
            self._lookup[key] = node
            self._reverse_lookup[node] = key
            self._trim_cache()
        # if it does we must move it to the front of the list
        else:
            self._prepend(node)
        # and update the value
            node.value = value

    def get(self, key: K) -> V | None:
        # update the value we found and move it to the front
        # return out the value or None if we didn't find it
        node: Node | None = self._lookup.get(key, None)
        if node:
            self._detach(node)
            self._prepend(node)
            return node.value
        else:
            return None

    def _detach(self, node: Node[T]) -> None:
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.head == node:
            self.head = self.head.prev
        if self.tail == node:
            self.tail = self.tail.next

    def _prepend(self, node: Node[T]) -> None:
        if self.head is None:
            self.head = self.tail = node
            return None
        else:
            self.head.next = node
            node.prev = self.head
            self.head = node

    def _trim_cache(self) -> None:
        if self.length > self.capacity:
            key: K = self._reverse_lookup[self.tail]
            del self._lookup[key]
            del self._reverse_lookup[self.tail]
            self._detach(self.tail)
            self.length -= 1
            return None
        else:
            return None

