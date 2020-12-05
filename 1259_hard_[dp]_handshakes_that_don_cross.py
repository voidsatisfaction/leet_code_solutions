from collections import defaultdict

class Solution:
    def numberOfWays(self, num_people: int) -> int:
        MOD = 10**9 + 7

        dp = defaultdict(int)
        dp[0] = 1
        dp[2] = 1
        
        for i in range(4, num_people+2, 2):
            for j in range(0, i, 2):
                dp[i] += (dp[i-j-2] * dp[j])
            dp[i] %= MOD

        return dp[num_people]

if __name__ == '__main__':
    s = Solution()
    assert s.numberOfWays(2) == 1
    assert s.numberOfWays(4) == 2