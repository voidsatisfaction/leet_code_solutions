from typing import List
from collections import defaultdict, Counter

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix_character_counter = defaultdict(Counter)

        for i, c in enumerate(s):
            if i > 0:
                prefix_character_counter[i] = prefix_character_counter[i] + prefix_character_counter[i-1]
            prefix_character_counter[i][c] += 1

        answer = []
        for [i, j, k] in queries:
            range_counter = prefix_character_counter[j] - prefix_character_counter[i-1]

            remain_character_count = 0
            for _, count in range_counter.items():
                if count % 2 == 1:
                    remain_character_count += 1

            needed_k = remain_character_count // 2

            if needed_k > k:
                answer.append(False)
            else:
                answer.append(True)

        return answer

if __name__ == '__main__':
    s = Solution()

    assert s.canMakePaliQueries('abcda', [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]) == [True, False, False, True, True]

    assert s.canMakePaliQueries('lyb', [[0,1,0],[2,2,1]]) == [False, True]
