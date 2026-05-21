from __future__ import annotations
import unittest
from binary_tree import BinaryTree

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt = BinaryTree()
        values: list[int] = [5,8,3,4,2,9,7]
        for value in values:
            self.bt.insert(value)

    def test_preorder_traversal(self):
        self.assertEqual(
                self.bt.preorder_traversal(self.bt.root),
                [5,3,2,4,8,7,9]
        )

    def test_inorder_traversal(self):
        self.assertEqual(
                self.bt.inorder_traversal(self.bt.root),
                [2,3,4,5,7,8,9]
        )

    def test_postorder_traversal(self):
        self.assertEqual(
                self.bt.postorder_traversal(self.bt.root),
                [2,4,3,7,9,8,5]
        )

    def test_breadth_first_search(self):
        self.assertTrue(self.bt.breadth_first_search(7))
        self.assertFalse(self.bt.breadth_first_search(99))

    def test_depth_first_search(self):
        self.assertTrue(self.bt.depth_first_search(7))
        self.assertFalse(self.bt.depth_first_search(99))

    def test_equal(self):
        same_tree: BinaryTree = BinaryTree()
        values: list[int] = [5,8,3,4,2,9,7]
        for value in values:
            same_tree.insert(value)

        diff_tree: BinaryTree = BinaryTree()
        values: list[int] = [5,8,3,4,2,1,7]
        for value in values:
            diff_tree.insert(value)
        self.assertTrue(self.bt == same_tree)
        self.assertFalse(self.bt == diff_tree)

    def test_delete(self):
        self.bt.delete(8)
        del_tree = BinaryTree()
        values: list[int] = [5,3,4,2,7,9]
        for value in values:
            del_tree.insert(value)
        self.assertTrue(self.bt == del_tree)




