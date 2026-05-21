from __future__ import annotations

class Node:
    def __init__(self):
        self.isWord: bool = False
        self.children: dict[str, Node] = {}

class Trie:
    def __init__(self):
        self.root: Node = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children.keys():
                curr = curr.children[c]
            else:
                node = Node()
                curr.children[c] = node
                curr = node
        curr.isWord = True

    def _delete_recursive(self, node: Node, word: str, depth: int) -> bool:
        # find the end of the word
        # base case: found end of word
        if depth == len(word):
            if not node.isWord:
                return False
            node.isWord = False
            return len(node.children) == 0

        char = word[depth]
        # word doesn't exist in tree
        if char not in node.children:
            return False

        should_delete_child: bool = self._delete_recursive(
                node.children[char],
                word,
                depth + 1
        )
        if should_delete_child:
            del node.children[char]
            # advise the parent node if this node can also be deleted
            return not node.isWord and len(node.children) == 0
        return False

    def delete(self, word: str) -> bool:
        return self._delete_recursive(self.root, word, 0)

    def _dfs(self, node: Node, prefix: str, results: list[str]):
        if node.isWord:
            results.append(prefix)
        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, results)

    def autocomplete(self, prefix: str) -> list[str]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        results = []
        self._dfs(node, prefix, results)
        return results


