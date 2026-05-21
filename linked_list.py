from __future__ import annotations
from typing import Generic, TypeVar, Optional
from dataclasses import dataclass

T = TypeVar('T')
@dataclass
class Node(Generic[T]):
    next: Node[T] | None
    prev: Node[T] | None
    value: T

class DoublyLinkedList:
    def __init__(self) -> None:
        self.length: int = 0
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None

    def prepend(self, item: T) -> None:
        node: Node[T] = Node(None, None, item)
        self.length += 1
        if not self.head:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at(self, item: T, index: int) -> None:
        if index > self.length:
            raise Exception(f'Index: {index} is > list length: {self.length}')
        elif index == self.length:
            self.append(item)
            return
        elif index == 0:
            self.prepend(item)
            return
        self.length += 1
        curr = self.get_at(index)
        node = Node(None, None, item)
        node.next = curr
        node.prev = curr.prev
        curr.prev = node
        node.prev.next = node

    def append(self, item: T) -> None:
        self.length += 1
        node: Node[T] = Node(None, None, item)
        if not self.tail:
            self.head = self.tail = node
            return None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def remove(self, item: T) -> T | None:
        curr = self.head
        i = 0
        while i < self.length and curr:
            if curr.value == item:
                break
            if curr.next:
                curr = curr.next
            i += 1
        return self.remove_node(curr)

    def get(self, index: int) -> T | None:
        node = self.get_at(index)
        if node:
            return node.value
        else:
            return None

    def remove_at(self, index: int) -> T | None:
        node = self.get_at(index)
        if not node:
            return None
        return self.remove_node(node)

    def remove_node(self, node: Node[T]) -> T | None:
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head == node.next
        if node == self.tail:
            self.tail == node.prev
        node.next = node.prev = None
        return node.value

    def get_at(self, index: int) -> Node[T] | None:
        curr = self.head
        i = 0
        while i < index and curr:
            if curr.next:
                curr = curr.next
            i += 1
        return curr

    def __str__(self) -> str:
        curr = self.head
        out = ''
        out += f'length: {self.length} \n'
        while True:
            curr = curr.next
            if not curr:
                break
            out += f'{curr.prev.value} => {curr.value} '
        return out







            
