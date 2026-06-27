import unittest
#from lru_cache import LRU
from quiz import LRU

class TestLRU(unittest.TestCase):
    def setUp(self):
        self.lru = LRU(3)

    def test_functionality(self):
        self.assertIsNone(self.lru.get('foo'))
        self.lru.update('foo', 69)
        self.assertEqual(self.lru.get('foo'), 69)
        self.lru.update('bar', 420)
        self.assertEqual(self.lru.get('bar'), 420)
        self.lru.update('baz', 999)
        self.assertEqual(self.lru.get('baz'), 999)
        self.lru.update('zaz', 555)
        self.assertIsNone(self.lru.get('foo'))


if __name__ == '__main__':
    unnittest.main()
