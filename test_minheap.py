import unittest
#from min_heap import MinHeap
from quiz import MinHeap

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.mh = MinHeap()
        self.values = [7,6,5,4,3,2,1]
        for v in self.values:
            self.mh.insert(v)

    def test_insert(self):
        self.assertEqual(self.mh.data[0], 1)
        self.assertEqual(self.mh.length, len(self.values))

    def test_pop(self):
        min_1 = self.mh.pop()
        min_2 = self.mh.pop()
        self.assertEqual(min_1, 1)
        self.assertEqual(min_2, 2)

        
