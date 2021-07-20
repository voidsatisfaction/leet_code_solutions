from typing import List
from collections import defaultdict

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word_to_index_list_map = defaultdict(list)

        for index, word in enumerate(wordsDict):
            word_to_index_list_map[word].append(index)

        word1_index_list, word2_index_list = \
            word_to_index_list_map[word1], word_to_index_list_map[word2]

        min_distance = len(wordsDict)
        if word1 == word2:
            i, j = 0, 1
            while j < len(word1_index_list):
                index1, index2 = word1_index_list[i], word1_index_list[j]
                current_distance = index2 - index1
                min_distance = min(min_distance, current_distance)
                i += 1
                j += 1
        else:
            i, j = 0, 0
            while i < len(word1_index_list) and j < len(word2_index_list):
                index1, index2 = word1_index_list[i], word2_index_list[j]
                current_distance = abs(index2 - index1)
                min_distance = min(min_distance, current_distance)
                if index1 > index2:
                    j += 1
                else:
                    i += 1

        return min_distance


if __name__ == '__main__':
    s = Solution()

    assert s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding") == 1

    assert s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes") == 3