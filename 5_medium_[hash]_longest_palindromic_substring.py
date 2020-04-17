from collections import defaultdict, deque

class Solution:
    def _is_palindrome(self, s: str) -> bool:
        reversed_s = s[::-1]

        return s == reversed_s

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        answer = s[0]

        location_cache = defaultdict(deque)

        for i, c in enumerate(s):
            location_cache[c].append(i)

        for i, c in enumerate(s):
            for c_index in reversed(location_cache[c]):
                if c_index-i+1 <= len(answer):
                    break
                
                if self._is_palindrome(s[i:c_index+1]):
                    answer = s[i:c_index+1]

            location_cache[c].popleft()

        return answer


if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("babadada"))