import unittest
#from linked_list import DoublyLinkedList
from quiz import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()
        for i in range(10):
            self.dll.append(i)

    def test_length(self):
        self.assertEqual(self.dll.length, 10)

    def test_get(self):
        self.assertEqual(self.dll.get(5), 5)

    def test_prepend(self):
        value = 99
        self.dll.prepend(99)
        self.assertEqual(self.dll.head.value, value)

    def test_append(self):
        value = 99
        self.dll.append(99)
        self.assertEqual(self.dll.tail.value, value)

    def test_insert_at(self):
        value = 99
        self.dll.insert_at(value, 5)
        self.assertEqual(self.dll.get(5), value)

    def test_remove(self):
        index = 5
        old_length = self.dll.length
        self.assertEqual(self.dll.remove(index), index)
        self.assertEqual(self.dll.length, old_length - 1)
        self.assertEqual(self.dll.get_at(index).value, index + 1)
        self.assertEqual(self.dll.get_at(index - 1).value, index - 1)


if __name__ == '__name__':
    unittest.main()
