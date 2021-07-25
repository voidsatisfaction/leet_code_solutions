from typing import List, Optional

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set()
        for word in wordDict:
            word_set.add(word)
        
        dp = [ [] for _ in range(len(s)+1) ]
        answer = self._dfs(0, s[0], word_set, s, dp)

        return answer

    def _dfs(self, index: int, current_word: str, word_set: set, s: str, dp: List[List[str]]) -> List[str]:
        if index == len(s)-1 and current_word not in word_set:
            return []

        if index == len(s)-1:
            return [current_word]

        if len(current_word) == 1 and len(dp[index]) > 0:
            return dp[index]

        result, temp = [], []
        if current_word in word_set:
            dp[index+1] = self._dfs(index+1, s[index+1], word_set, s, dp)

            temp = [*dp[index+1]]
            for sentence in temp:
                result.append(current_word + ' ' + sentence)

        result += self._dfs(index+1, current_word+s[index+1], word_set, s, dp)

        return result
        

if __name__ == '__main__':
    s = Solution()

    assert sorted(s.wordBreak('catsanddog', ["cat","cats","and","sand","dog"])) == sorted(["cats and dog","cat sand dog"])

    assert sorted(s.wordBreak('pineapplepenapple', ["apple","pen","applepen","pine","pineapple"])) == sorted(["pine apple pen apple","pineapple pen apple","pine applepen apple"])

    assert s.wordBreak('catsandog', ["cats","dog","sand","and","cat"]) == []
