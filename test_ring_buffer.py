import unittest
from ring_buffer import RingBuffer

class TestRingBuffer(unittest.TestCase):
    def setUp(self):
        self.rb: RingBuffer = RingBuffer(3)
        self.rb.append('A')
        self.rb.append('B')
        self.rb.append('C')

    def test_append(self):
        self.assertEqual(self.rb.buffer, ['A','B','C'])
        self.assertEqual(self.rb.head, 0)
        self.assertEqual(self.rb.tail, 0)

    def test_overwrite(self):
        self.rb.append('D')
        self.assertEqual(str(self.rb), "RingBuffer(['B', 'C', 'D'])")
        self.assertEqual(self.rb.head, 1)
        self.assertEqual(self.rb.tail, 1)

    def test_pop(self):
        oldest = self.rb.pop()
        self.assertEqual(oldest, 'A')
        self.assertEqual(str(self.rb), 'RingBuffer([\'B\', \'C\'])')

        

