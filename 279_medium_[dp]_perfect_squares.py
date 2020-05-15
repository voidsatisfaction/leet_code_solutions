from math import inf

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [ inf for _ in range(n+1) ]
        dp[0] = 0

        for i in range(1, n+1):
            for j in range(1, n+1):
                index = i-j*j

                if index < 0:
                    break

                dp[i] = min(dp[i], dp[index] + 1)

        return dp[n]

if __name__ == '__main__':
    assert Solution().numSquares(1) == 1
    assert Solution().numSquares(4) == 1
    assert Solution().numSquares(12) == 3
    assert Solution().numSquares(13) == 2