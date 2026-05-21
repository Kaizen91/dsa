from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional
from data_structures import Queue

T = TypeVar('T')


@dataclass
class TreeNode:
    value: T | None
    left: TreeNode[T] | None
    right: TreeNode[T] | None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def __str__(self):
        if not self.root:
            return 'empty tree'
        else:
            return self._build_output_string(self.root, level = 0)

    def _build_output_string(self, node: Treenode, level: int) -> str:
        if not node:
            return ''
        out = ''
        out += self._build_output_string(node.right, level + 1)
        indent = '      ' * level
        out += f"{indent}└── {node.value}\n"
        out += self._build_output_string(node.left, level + 1)
        return out
        

    def insert(self, value: T) -> None:
        if not self.root:
            self.root = TreeNode(value, None, None)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode[T], value: T) -> None:
        if value <= node.value:
            if not node.left:
                node.left = TreeNode(value, None, None)
            else:
                self._insert_recursive(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value, None, None)
            else:
                self._insert_recursive(node.right, value)

    def _delete_recursive(self, root: TreeNode, value: T) -> TreeNode | None:
        #base case
        if root is None:
            return root
        # find node
        if value < root.value:
            root.left = self._delete_recursive(root.left, value)
        elif value > root.value:
            root.right = self._delete_recursive(root.right, value)
            
        else: # found node
            # Cases 1 & 2:
            # if the node has one child just move it up
            # otherwise if it's None move it up and it's the
            # same as just deleting
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: two children
            successor: TreeNode = self._find_max(root.left)
            root.value = successor.value
            root.left = self._delete_recursive(root.left, successor.value)
        return root

    def _find_max(self, root: TreeNode) -> TreeNode:
        curr = root
        while curr.right is not None:
            curr = curr.right
        return curr
            
    def delete(self, value: T) -> None:
        self.root = self._delete_recursive(self.root, value)

    def _invert_recursive(self, node: TreeNode) -> None:
        if node is None:
            return None
        node.left, node.right = node.right, node.left
        self._invert_recursive(node.left)
        self._invert_recursive(node.right)
        return node

    def invert(self) -> TreeNode | None:
        return self._invert_recursive(self.root)

    def inorder_traversal(
        self, node: TreeNode[T], result: list[T] | None = None
    ) -> list[T] | None:
        if result is None:
            result: list[T] = []

        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

        return result

    def preorder_traversal(
        self, node: TreeNode[T], result: list[T] | None = None
    ) -> list[T] | None:
        if result is None:
            result: list[T] = []

        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

        return result

    def postorder_traversal(
        self, node: TreeNode[T], result: list[T] | None = None
    ) -> list[T] | None:
        if result is None:
            result: list[T] = []

        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)

        return result

    def breadth_first_search(self, needle: T) -> TreeNode | bool:
        q: Queue = Queue()
        q.enqueue(self.root)
        while q.length:
            curr = q.deque()
            if curr.value == needle:
                return curr
            if curr.left:
                q.enqueue(curr.left)
            if curr.right:
                q.enqueue(curr.right)
        return False


    def _walk_recursive(self, node: TreeNode, needle: T) -> TreeNode | bool:
        if node is None:
            return False
        if node.value == needle:
            return node
        if node.value > needle:
            return self._walk_recursive(node.left, needle)
        else:
            return self._walk_recursive(node.right, needle)

    def depth_first_search(self, needle: T) ->  bool:
        return self._walk_recursive(self.root, needle)

    def _compare(self, a: TreeNode, b: TreeNode) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.value != b.value:
            return False
        return self._compare(a.left, b.left) and self._compare(
            a.right, b.right
        )

    def __eq__(self, other: BinaryTree) -> bool:
        return self._compare(self.root, other.root)
