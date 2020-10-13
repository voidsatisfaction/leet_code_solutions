class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        A = 2
        L = 3

        dp = [ [ [ 0 for _ in range(L) ] for _ in range(A) ] for _ in range(n+1) ]

        dp[0][0][0] = 1

        for i in range(1, n+1):
            for a in range(A):
                for l in range(L):
                    if a == 0:
                        if l == 0:
                            dp[i][a][l] = (dp[i-1][a][0] + dp[i-1][a][1] + dp[i-1][a][2]) % MOD
                        elif l == 1:
                            dp[i][a][l] = dp[i-1][a][0]
                        else:
                            dp[i][a][l] = dp[i-1][a][1]
                    else:
                        if l == 0:
                            dp[i][a][l] = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2] \
                                + dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2]) % MOD
                        elif l == 1:
                            dp[i][a][l] = dp[i-1][1][0]
                        else:
                            dp[i][a][l] = dp[i-1][1][1]

        answer = 0
        for a in range(A):
            for l in range(L):
                answer += dp[n][a][l]

        return answer % MOD


if __name__ == '__main__':
    s = Solution()

    assert s.checkRecord(2) == 8