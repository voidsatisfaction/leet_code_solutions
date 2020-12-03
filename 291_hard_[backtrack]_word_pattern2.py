class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        s_look_up_table = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                s_look_up_table[(i, j)] = s[i:j+1]

        return self._dfs(
            s,
            pattern,
            0,
            0,
            {},
            {},
            s_look_up_table
        )

    def _dfs(
        self,
        s: str,
        pattern: str,
        i: int,
        j: int,
        char_to_word_map: dict,
        word_to_char_map: dict,
        s_look_up_table: dict
    ) -> bool:
        if i == len(s) and j == len(pattern):
            return True

        if i == len(s) or j == len(pattern):
            return False

        pattern_char = pattern[j]

        if pattern_char in char_to_word_map:
            pattern_char_word = char_to_word_map[pattern_char]
            pattern_char_word_length = len(pattern_char_word)

            if s_look_up_table.get((i, i+pattern_char_word_length-1)) is not None and \
                s_look_up_table.get((i, i+pattern_char_word_length-1)) == pattern_char_word:

                return self._dfs(
                    s,
                    pattern,
                    i+pattern_char_word_length,
                    j+1,
                    char_to_word_map,
                    word_to_char_map,
                    s_look_up_table
                )
            else:
                return False
        else:
            result = False
            for k in range(len(s)-i):
                word = s_look_up_table.get((i, i+k))
                if word in word_to_char_map:
                    continue

                char_to_word_map[pattern_char] = word
                word_to_char_map[word] = pattern_char

                result |= self._dfs(
                    s,
                    pattern,
                    i+k+1,
                    j+1,
                    char_to_word_map,
                    word_to_char_map,
                    s_look_up_table
                )

                del char_to_word_map[pattern_char]
                del word_to_char_map[word]

            return result

if __name__ == '__main__':
    s = Solution()
    assert s.wordPatternMatch('abab', 'redblueredblue') is True
    assert s.wordPatternMatch('aaaa', 'asdasdasdasd') is True
    assert s.wordPatternMatch('abab', 'asdasdasdasd') is True
    assert s.wordPatternMatch('aabb', 'xyzabcxzyabc') is False

    assert s.wordPatternMatch('a', '') is False
    assert s.wordPatternMatch('ab', 'aa') is False