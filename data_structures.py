from __future__ import annotations
from typing import Generic, TypeVar, Optional
from dataclasses import dataclass

T = TypeVar('T')
class Node(Generic[T]):
    def __init__(self, next, value, parent=None):
        self.next: Node | None = next
        self.value: T = value
        self.parent: Node | None = parent


class Queue():
    def __init__(self):
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None
        self.length = 0

    def enqueue(self, item: T):
        if not self.tail:
            self.head = Node(None, item)
            self.tail = self.head 
        else:
            tmp: Node[T] = Node(None, item)
            self.tail.next = tmp
            self.tail = tmp
        self.length += 1

    def deque(self):
        if not self.head:
            raise ValueError('empty queue')
        self.length -= 1
        res: Node[T] = self.head
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = self.tail = None
        return res.value

    def peek(self):
        if self.head:
            return self.head.value
        else:
            raise ValueError('empty queue')


class Stack:
    def __init__(self):
        self.tail: Node[T] | None = None
        self.length: int = 0

    def push(self, item: T):
        if not self.tail:
            self.tail = Node(None, item)
        else:
            tmp: Node[T] = Node(self.tail, item)
            self.tail = tmp
        self.length += 1

    def pop(self):
        if not self.tail:
            raise ValueError('empty queue')
        self.length -= 1
        res: Node[T] = self.tail
        self.tail = self.tail.next
        return res.value

    def peek(self):
        if self.tail:
            return self.tail.value
        else:
            raise ValueError('empty queue')



