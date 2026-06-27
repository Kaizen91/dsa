import unittest  
#from trie import Trie
from quiz import Trie

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
                self.t.autocomplete('ca'),
                ['cat','cattle','cart'],
        )

    def test_delete(self):
        self.t.delete('cat')
        self.t.delete('cattle')
        self.t.delete('cart')
        self.assertEqual(
                self.t.autocomplete('ca'),
                []
        )
        self.t.insert('cat')
        self.t.insert('cattle')
        self.t.delete('cat')
        self.assertEqual(
                self.t.autocomplete('ca'),
                ['cattle']
        )
        self.t.insert('car')
        self.t.delete('car')
        self.assertNotIn(
                'r',
                self.t.root.children['c'].children['a'].children.keys()
        )

        

