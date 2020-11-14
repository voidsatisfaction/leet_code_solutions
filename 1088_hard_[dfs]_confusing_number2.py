class Solution:
    def confusingNumberII(self, N: int) -> int:
        ans = 0
        ans += self._dfs(1, 1, 1, N)
        ans += self._dfs(6, 9, 1, N)
        ans += self._dfs(8, 8, 1, N)
        ans += self._dfs(9, 6, 1, N)
        
        return ans

    def _dfs(self, n: int, rotated_n: int, digit: int, N: int) -> int:
        rotate_map = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }

        count = 0

        if n > N:
            return count

        for next_number in rotate_map:
            next_rotated_number = rotate_map[next_number]

            next_n = n * 10 + next_number
            next_rotated_n = next_rotated_number * (10 ** digit) + rotated_n

            count += self._dfs(next_n, next_rotated_n, digit+1, N)

        if n != rotated_n:
            count += 1

        return count

if __name__ == '__main__':
    s = Solution()
    assert s.confusingNumberII(20) == 6
    assert s.confusingNumberII(100) == 19
    assert s.confusingNumberII(1) == 0