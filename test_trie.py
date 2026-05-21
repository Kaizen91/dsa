import unittest  
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t: Trie = Trie()
        words: list[str] = [
                'cat',
                'cart',
                'cattle',
                'apple',
                'dog',
                'doge',
        ]
        for word in words:
            self.t.insert(word)

    def test_autocomplete(self):
        self.assertEqual(
                self.t.autocomplete('ca').sort(),
                ['cat','cattle','cart'].sort()
        )

    def test_delete(self):
        self.t.delete('cat')
        self.t.delete('cattle')
        self.t.delete('cart')
        self.assertEqual(
                self.t.autocomplete('ca'),
                []
        )
        

