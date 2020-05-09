class Node:
    def __init__(self, val, is_word=False):
        self.val = val
        self.children = {}
        self.is_word = is_word

class Trie:

    def __init__(self):
        self.children = {}
        

    def insert(self, word: str) -> None:
        last_node = self
        for c in word:
            if not last_node.children.get(c):
                last_node.children[c] = Node(c)

            last_node = last_node.children[c]

        last_node.is_word = True
        

    def search(self, word: str) -> bool:
        last_node = self._search_prefix(word)

        return last_node is not None and last_node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        last_node = self._search_prefix(prefix)

        return last_node is not None

    def _search_prefix(self, prefix: str) -> bool:
        last_node = self
        for c in prefix:
            if not last_node.children.get(c):
                return None

            last_node = last_node.children[c]

        return last_node
        

if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    trie = Trie();

    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    trie.insert("app")
    assert trie.search("app") == True

    trie = Trie()

    trie.insert("a")
    assert trie.search("a") == True
    assert trie.startsWith("a") == True