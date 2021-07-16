from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[[0, 0] for _ in range(2)] for _ in range(n)]
        dp[0][1][1] = nums[0]

        for i in range(1, n):
            if i == n-1:
                dp[i][0][0] = max(dp[i-1][1][0], dp[i-1][0][0])
                dp[i][0][1] = max(dp[i-1][1][1], dp[i-1][0][1])
                dp[i][1][0] = dp[i-1][0][0] + nums[i]
                dp[i][1][1] = -1
            else:
                dp[i][0][0] = max(dp[i-1][1][0], dp[i-1][0][0])
                dp[i][0][1] = max(dp[i-1][1][1], dp[i-1][0][1])
                dp[i][1][0] = dp[i-1][0][0] + nums[i]
                dp[i][1][1] = dp[i-1][0][1] + nums[i]

        answer = max(
            dp[n-1][0][0],
            dp[n-1][0][1],
            dp[n-1][1][0],
            dp[n-1][1][1]
        )

        return answer

if __name__ == '__main__':
    s = Solution()

    assert s.rob([2,3,2]) == 3

    assert s.rob([1,2,3,1]) == 4

    assert s.rob([0]) == 0

    assert s.rob([1]) == 1