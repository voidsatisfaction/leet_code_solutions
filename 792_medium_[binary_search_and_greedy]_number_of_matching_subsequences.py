from typing import List
from collections import defaultdict
from bisect import bisect_right

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        character_location = defaultdict(list)

        for index, c in enumerate(s):
            character_location[c].append(index)

        answer = 0
        for word in words:
            current_index, is_valid = -1, True
            for c in word:
                character_location_index = bisect_right(character_location[c], current_index)
                if character_location_index == len(character_location[c]):
                    is_valid = False
                    break

                current_index = character_location[c][character_location_index]
            
            if is_valid:
                answer += 1

        return answer


if __name__ == '__main__':
    s = Solution()

    assert s.numMatchingSubseq('abcde', ['a', 'bb', 'acd', 'ace']) == 3

    assert s.numMatchingSubseq('dsahjpjauf', ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]) == 2
