from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0 -> cooldown
        # 1 -> buy
        # 2 -> sell
        dp = [0, -inf, -inf]
        for price in prices:
            next_dp = [0, 0, 0]

            next_dp[0] = max(dp[0], dp[2])
            next_dp[1] = max(dp[0]-price, dp[1])
            next_dp[2] = dp[1]+price

            dp = next_dp

        return max(dp)

if __name__ == '__main__':
    assert Solution().maxProfit([1]) == 0
    assert Solution().maxProfit([1, 2]) == 1
    assert Solution().maxProfit([1,2,3,0,2]) == 3