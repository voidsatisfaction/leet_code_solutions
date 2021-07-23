from typing import List, Tuple
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self._children = defaultdict(TrieNode)
        self._sentence_list = []

    def add_child_and_sentence(self, c: str, sentence: str) -> None:
        child = self.get_child(c)
        child._sentence_list.append(sentence)

    def get_child(self, c: str) -> 'TrieNode':
        return self._children[c]

    def get_sentence_list(self) -> List[str]:
        return self._sentence_list


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self._trie = TrieNode()
        self._sentence_count = defaultdict(int)

        sentence_time_list = zip(sentences, times)
        for sentence, time in sentence_time_list:
            self._sentence_count[sentence] += time

        self._construct_trie_from_sentence_list(self._trie, sentences)

        self._current_query = ''

        self._top = 3

    def input(self, c: str) -> List[str]:
        self._current_query += c

        return self._get_auto_complete(self._current_query, self._top)

    def _reset_current_query(self) -> None:
        self._current_query = ''

    def _get_auto_complete(self, query: str, top: int) -> List[str]:
        current_trie_node = self._trie
        for c in query:
            if c == '#':
                self._add_new_sentence(query[:-1])
                self._reset_current_query()
                return []
            else:
                current_trie_node = current_trie_node.get_child(c)

        return self._get_top_k_sentence_of(current_trie_node, top)

    def _get_top_k_sentence_of(self, trie_node: TrieNode, k: int) -> List[str]:
        sentence_list = trie_node.get_sentence_list()
        return [ sentence for sentence in sorted(sentence_list, key=lambda s: (-self._sentence_count[s], s))[:k] ]

    def _add_new_sentence(self, sentence: str) -> None:
        if self._sentence_count[sentence] == 0:
            self._construct_trie_from_sentence_list(self._trie, [sentence])
        self._sentence_count[sentence] += 1

    def _construct_trie_from_sentence_list(self, trie: TrieNode, sentence_list: str) -> None:
        for sentence in sentence_list:
            current_node = trie
            for c in sentence:
                current_node \
                    .add_child_and_sentence(c, sentence)

                current_node = current_node.get_child(c)


if __name__ == '__main__':
    autocomplete_system = AutocompleteSystem(
        ["i love you", "island", "iroman", "i love leetcode"],
        [5, 3, 2, 2]
    )

    assert autocomplete_system.input('i') == ["i love you", "island", "i love leetcode"]

    assert autocomplete_system.input(' ') == ["i love you", "i love leetcode"]

    assert autocomplete_system.input('a') == []

    assert autocomplete_system.input('#') == []

    assert autocomplete_system.input('i') == ["i love you", "island", "i love leetcode"]

    assert autocomplete_system.input(' ') == ["i love you", "i love leetcode", "i a"]

    assert autocomplete_system.input('a') == ["i a"]

    assert autocomplete_system.input('#') == []
