from __future__ import annotations
from dataclasses import dataclass
from typing import TypeVar

V = TypeVar('V')
K = TypeVar('K')

@dataclass(eq = False)
class Node:
    prev: Node
    next: Node
    value: V


class LRU:
    def __init__(self, capacity: int):
        self.head: Node | None
        self.tail: Node | None
        self.length: int = 0
        self.head = self.tail = None
        self._lookup: dict[K, Node[T]] = {}
        self._reverse_lookup: dict[Node[T], K] = {}
        self.capacity = capacity

    def update(self, key: K, value: V) -> None:
        #check the cache for existence
        # use get
        node = self._lookup.get(key, None)
        # if it doesn't then we insert
        #   - check capacity and evict if we are at capacity
        if node is None:
            node = Node(None, None, value)
            self.length += 1
            self._prepend(node)
            self._trim_cache()
            self._lookup[key] = node
            self._reverse_lookup[node] = key
        # if it does we must move it to the front of the list
        # and update the value
        else:
            self._detach(node)
            self._prepend(node)
            node.value = value
        
    def get(self, key: K) -> V | None:
        #check the cache for existence
        node = self._lookup.get(key, None)
        if node is None:
            return None

        # update the value we found and move it to the front
        self._detach(node)
        self._prepend(node)
        # return out the value or None if we didn't find it
        return node.value

    def _detach(self, node: Node[T]) -> None:
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        node.next = None
        node.prev = None

    def _prepend(self, node: Node[T]) -> None:
        if self.head is None:
            self.head = self.tail = node
            return None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def _trim_cache(self) -> None:
        if self.length <= self.capacity:
            return None
        tail = self.tail
        self._detach(self.tail)
        key = self._reverse_lookup[tail]
        del self._lookup[key]
        del self._reverse_lookup[tail]
        self.length -= 1
        return None
