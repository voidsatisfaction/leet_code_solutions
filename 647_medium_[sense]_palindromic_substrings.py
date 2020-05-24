class Solution:
    def countSubstrings(self, s: str) -> int:
        s_len = len(s)
        if s_len == 1:
            return 1

        answer = 0
        candidates = []

        for left in range(s_len):
            candidates.append((left, left))
            answer += 1

            if left == s_len-1 or s[left] != s[left+1]:
                continue
            candidates.append((left, left+1))
            answer += 1

        while len(candidates) > 0:
            (left, right) = candidates.pop()

            if left <= 0 or right >= s_len-1:
                continue

            next_left, next_right = left-1, right+1
            if s[next_left] != s[next_right]:
                continue

            candidates.append((next_left, next_right))
            answer += 1

        return answer

if __name__ == '__main__':
    assert Solution().countSubstrings('abc') == 3
    assert Solution().countSubstrings('aaa') == 6