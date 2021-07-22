import string
from typing import List
from collections import defaultdict, namedtuple

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        adjacent_list = self._create_adjacent_list([beginWord, *wordList])

        self._bfs(beginWord, endWord, adjacent_list)

        answer = self._backtrack(beginWord, endWord, adjacent_list)

        return answer

    def _create_adjacent_list(self, wordList: List[str]) -> defaultdict:
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

    def _bfs(self, beginWord: str, endWord: str, adjacent_list: defaultdict) -> None:
        queue, visited, is_finished = [beginWord], set(), False

        while len(queue) > 0:
            next_queue = []
            for word in queue:
                already_visited_adjacent_word_list = []
                for adjacent_word in adjacent_list[word]:
                    if word in adjacent_list[adjacent_word]:
                        adjacent_list[adjacent_word].remove(word)

                    if adjacent_word in visited:
                        already_visited_adjacent_word_list.append(adjacent_word)

                for adjacent_word in already_visited_adjacent_word_list:
                    adjacent_list[word].remove(adjacent_word)

            for word in queue:
                for adjacent_word in adjacent_list[word]:
                    visited.add(adjacent_word)
                    next_queue.append(adjacent_word)

            queue = next_queue

    def _backtrack(self, beginWord: str, endWord: str, dag_adjacent_list: defaultdict) -> List[List[str]]:
        def _backtrack_rec(word: str, endWord: str, path: List[str], dag_adjacent_list: defaultdict, answer: List[List[str]]) -> None:
            if word == endWord:
                answer.append([*path])
                return

            for adjacent_word in dag_adjacent_list[word]:
                path.append(adjacent_word)
                _backtrack_rec(adjacent_word, endWord, path, dag_adjacent_list, answer)
                path.pop()

        answer, path = [], [beginWord]

        _backtrack_rec(beginWord, endWord, path, dag_adjacent_list, answer)

        return answer


if __name__ == '__main__':
    s = Solution()

    assert s.findLadders('dog', 'cog', ["cog"]) == [['dog', 'cog']]

    assert sorted(s.findLadders('hit', 'cog', ['hot','dot','dog','lot','log','cog'])) == sorted([["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]])

    assert s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log"]) == []

    assert sorted(s.findLadders('red', 'tax', ["ted","tex","red","tax","tad","den","rex","pee"])) == sorted([["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]])
