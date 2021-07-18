from typing import List

from collections import defaultdict

class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self._word_to_index_list_map = defaultdict(list)
        self._max_distance = 3 * (10 ** 4)

        for index, word in enumerate(wordsDict):
            self._word_to_index_list_map[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        word1_sorted_index_list, word2_sorted_index_list = \
            self._word_to_index_list_map[word1], self._word_to_index_list_map[word2]

        minimum_distance = self._max_distance

        i, j = 0, 0
        while i < len(word1_sorted_index_list) and j < len(word2_sorted_index_list):
            word1_index, word2_index = word1_sorted_index_list[i], word2_sorted_index_list[j]
            distance = abs(word1_index-word2_index)

            minimum_distance = min(minimum_distance, distance)

            if word1_index > word2_index:
                j += 1
            else:
                i += 1

        return minimum_distance


if __name__ == '__main__':
    wd = WordDistance(["practice", "makes", "perfect", "coding", "makes"])

    assert wd.shortest("coding", "practice") == 3

    assert wd.shortest("makes", "coding") == 1
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)