class Solution:
    def countSubstrings(self, s: str) -> int:
        string_length = len(s)
        dp = [ [ False for _ in range(string_length) ] for _ in range(string_length) ]

        answer = 0
        for length in range(1, string_length+1):
            for i in range(string_length-length+1):
                j = i+length-1

                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]

                if dp[i][j] is True:
                    answer += 1

        return answer

if __name__ == '__main__':
    s = Solution()

    assert s.countSubstrings('abc') == 3

    assert s.countSubstrings('aaa') == 6
