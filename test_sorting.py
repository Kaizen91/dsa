import unittest
from sorting import bubblesort, quicksort, mergesort

class TestSort(unittest.TestCase):
    def setUp(self):
        self.arr = [5,7,4,8,3,1,6,9,0,2]
        self.sorted = [0,1,2,3,4,5,6,7,8,9]

    def test_bubblesort(self):
        bubblesort(self.arr)
        self.assertEqual(self.arr, self.sorted)

    def test_quicksort(self):
        quicksort(self.arr, 0, len(self.arr) - 1)
        self.assertEqual(self.arr, self.sorted)

    def test_mergesort(self):
        res = mergesort(self.arr)
        self.assertEqual(res, self.sorted)
        
if __name__ == '__main__':
    unnittest.main()
