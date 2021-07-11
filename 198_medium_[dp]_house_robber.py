from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(*nums)

        n = len(nums)

        dp = [[0, 0] for _ in range(n)]
        dp[0][0], dp[0][1] = 0, nums[0]
        dp[1][0], dp[1][1] = nums[0], nums[1]

        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]

        return max(dp[n-2][0], dp[n-2][1], dp[n-1][0], dp[n-1][1])

if __name__ == '__main__':
    s = Solution()

    assert s.rob([1]) == 1

    assert s.rob([1, 3]) == 3

    assert s.rob([1, 2, 3, 1]) == 4

    assert s.rob([2, 7, 9, 3, 1]) == 12