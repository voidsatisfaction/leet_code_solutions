import string
from typing import List
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjacent_list = self._create_adjacent_list([beginWord, *wordList])

        answer = self._bfs(beginWord, endWord, adjacent_list)

        return answer

    def _create_adjacent_list(self, wordList: [str]) -> defaultdict:
        def get_possible_adjacent_word_list(word: str) -> List[str]:
            adjacent_word_list = []
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word == word:
                        continue
                    adjacent_word_list.append(new_word)

            return adjacent_word_list

        word_list_set = set()
        for word in wordList:
            word_list_set.add(word)

        adjacent_list = defaultdict(set)
        for word in wordList:
            possible_adjacent_word_list = get_possible_adjacent_word_list(word)

            for adjacent_word in possible_adjacent_word_list:
                if adjacent_word in word_list_set:
                    adjacent_list[word].add(adjacent_word)
                    adjacent_list[adjacent_word].add(word)

        return adjacent_list

    def _bfs(self, beginWord: str, endWord: str, adjacent_list: defaultdict) -> int:
        queue, visited, distance = [beginWord], set([beginWord]), 1

        while len(queue) > 0:
            next_queue = []
            for word in queue:
                if word == endWord:
                    return distance

                for adjacent_word in adjacent_list[word]:
                    if adjacent_word in visited:
                        continue

                    visited.add(adjacent_word)
                    next_queue.append(adjacent_word)

            queue = next_queue
            distance += 1

        return 0

if __name__ == '__main__':
    s = Solution()

    assert s.ladderLength('dog', 'cog', ["cog"]) == 2

    assert s.ladderLength('hit', 'cog', ['hot','dot','dog','lot','log','cog']) == 5

    assert s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]) == 0

    assert s.ladderLength('hit', 'cog', ["hot","cog","dot","dog","hit","lot","log"]) == 5