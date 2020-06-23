class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def trim_p(p: str) -> str:
            trimmed_p = ''
            prev = ''

            for c in p:
                if c == '*' and prev == '*':
                    continue

                if c == '*':
                    trimmed_p += '*'
                    prev = '*'
                    continue

                prev = c
                trimmed_p += c

            return trimmed_p

        p = trim_p(p)
        p_length, s_length = len(p), len(s)

        if p_length == 0 and s_length == 0:
            return True

        if p_length == 0:
            return False

        visited = [[ False for _ in range(s_length)] for _ in range(p_length)]
        dp = [[ False for _ in range(s_length)] for _ in range(p_length)]

        def dfs(p_index, s_index, visited, dp) -> bool:
            if s_index == s_length:
                for p_i in range(p_index, p_length):
                    if p[p_i] != '*':
                        return False

                return True

            if visited[p_index][s_index] is True:
                return dp[p_index][s_index]

            visited[p_index][s_index] = True

            if p_index == p_length-1:
                if p[p_index] == '*':
                    return True

                if s_index == s_length-1 and (p[p_index] == '?' or p[p_index] == s[s_index]):
                    return True

                dp[p_index][s_index] = False
                return dp[p_index][s_index]

            if p[p_index] == '?':
                dp[p_index][s_index] = dfs(p_index+1, s_index+1, visited, dp)
            elif p[p_index] == '*':
                for s_i in range(s_index, s_length):
                    dp[p_index][s_index] = dp[p_index][s_index] or dfs(p_index+1, s_i, visited, dp)
            else:
                if p[p_index] != s[s_index]:
                    dp[p_index][s_index] = False
                else:
                    dp[p_index][s_index] = dfs(p_index+1, s_index+1, visited, dp)

            return dp[p_index][s_index]

        return dfs(0, 0, visited, dp)

if __name__ == '__main__':
    s = Solution()

    assert s.isMatch('aa', 'a') is False
    assert s.isMatch('aa', '*') is True
    assert s.isMatch('cb', '?a') is False
    assert s.isMatch('adceb', '*a*b') is True
    assert s.isMatch('acdcb', 'a*c?b') is False

    assert s.isMatch('', '') is True
    assert s.isMatch('a', '') is False
    assert s.isMatch('abc', '*****') is True

    assert s.isMatch(
        "bbabbaabbbabaaaabbbbabbaabbaaabbbbabbbaaaaaaaaaababbbabaabaabbbabbbaaabaababbbbababaaaaabaaaabbbbabbaaabbaaabbaabbbbababaaaaabbbbaaabababbbaabbbbaabbaabbabbbaabbababaaabbabbbaababbbbaaaabbababbbbabaaa",
        "**baab*a*bb*bbbbba********b***a******b*b*aaabbb*b*ba*a*b*a****b*babbba*aa*ababa*bb***babb*ab*b*abab*aa"
    ) is False