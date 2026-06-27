import unittest
#from data_structures import Queue, Stack
from quiz import Queue, Stack

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_length(self):
        self.assertEqual(self.q.length, 0)
        self.q.enqueue(1)
        self.assertEqual(self.q.length, 1)

    def test_enqueue_deque(self):
        for i in range(1,4):
            self.q.enqueue(i)
        self.assertEqual(self.q.deque(), 1)
        self.assertEqual(self.q.deque(), 2)
        self.assertEqual(self.q.deque(), 3)

    def test_peek(self):
        self.q.enqueue(1)
        self.assertEqual(self.q.peek(), 1)

class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_length(self):
        self.assertEqual(self.s.length, 0)
        self.s.push(1)
        self.assertEqual(self.s.length, 1)

    def test_push_pop(self):
        for i in range(1,4):
            self.s.push(i)
        self.assertEqual(self.s.pop(), 3)
        self.assertEqual(self.s.pop(), 2)
        self.assertEqual(self.s.pop(), 1)

    def test_peek(self):
        self.s.push(1)
        self.s.push(2)
        self.assertEqual(self.s.peek(), 2)

            
if __name__ == '__main__':
    unittest.main()
