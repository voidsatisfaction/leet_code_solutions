class Solution:
    def numSplits(self, s: str) -> int:
        left_char_to_count_map = {}
        right_char_to_count_map = {}

        for char in s:
            if right_char_to_count_map.get(char) is None:
                right_char_to_count_map[char] = 1
            else:
                right_char_to_count_map[char] += 1

        i = 0
        answer = 0
        while i <= len(s)-1:
            char = s[i]
            if left_char_to_count_map.get(char) is None:
                left_char_to_count_map[s[i]] = 1

            right_char_to_count_map[char] -= 1
            if right_char_to_count_map[char] == 0:
                del right_char_to_count_map[char]

            if len(left_char_to_count_map.keys()) == len(right_char_to_count_map.keys()):
                answer += 1

            i += 1

        return answer


if __name__ == '__main__':
    s = Solution()

    assert s.numSplits("aacaba") == 2

    assert s.numSplits("abcd") == 1

    assert s.numSplits("aaaaa") == 4

    assert s.numSplits("acbadbaada") == 2
