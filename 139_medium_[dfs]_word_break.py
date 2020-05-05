from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def word_break_rec(s: str) -> bool:
            if len(s) == 0:
                return True

            if s in dp:
                return False

            for index in range(len(s)):
                sub_string = s[0:index+1]
                if sub_string in word_set and word_break_rec(s[index+1:]):
                    return True

            dp[s] = False
            
            return False

        dp = {}
        word_set = {}

        for word in wordDict:
            word_set[word] = True

        return word_break_rec(s)

if __name__ == '__main__':
    print(Solution().wordBreak('a', ['aa']))