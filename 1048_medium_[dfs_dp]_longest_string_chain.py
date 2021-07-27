from typing import List
from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}

        adj_list = self._get_adj_list(words)

        answer = 0
        for word in words:
            answer = max(answer, self._dfs(word, adj_list, dp))

        return answer

    def _dfs(self, word: str, adj_list: defaultdict, dp: dict) -> int:
        if len(adj_list[word]) == 0:
            return 1

        if word in dp:
            return dp[word]

        dp[word] = 0
        for adj_word in adj_list[word]:
            dp[word] = max(dp[word], self._dfs(adj_word, adj_list, dp) + 1)

        return dp[word]

    def _get_adj_list(self, words: List[str]) -> defaultdict:
        adj_list = defaultdict(set)

        for word1 in words:
            for word2 in words:
                if self._is_adjacent_word(word1, word2):
                    adj_list[word1].add(word2)

        return adj_list

    def _is_adjacent_word(self, word1: str, word2: str) -> bool:
        if not len(word1)+1 == len(word2):
            return False

        for i in range(len(word2)):
            candidate = word2[:i] + word2[i+1:]
            if word1 == candidate:
                return True

        return False


if __name__ == '__main__':
    s = Solution()

    assert s.longestStrChain(["a","b","ba","bca","bda","bdca"]) == 4

    assert s.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]) == 5

    assert s.longestStrChain(["abcd","dbqca"]) == 1