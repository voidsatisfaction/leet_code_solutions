from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [ [1, 1] for _ in range(len(nums)) ]

        global_max_length = 1
        for i, num in enumerate(nums):
            current_max_length, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    current_max_length = max(current_max_length, dp[j][0]+1)

            for j in range(i):
                if nums[j] < num and dp[j][0] == current_max_length-1:
                    count += dp[j][1]

            dp[i] = [current_max_length, max(count, dp[i][1])]
            global_max_length = max(global_max_length, current_max_length)

        answer = 0
        for i in range(len(nums)):
            if dp[i][0] == global_max_length:
                answer += dp[i][1]

        return answer

if __name__ == '__main__':
    s = Solution()

    assert s.findNumberOfLIS([1, 3, 5, 4, 7]) == 2

    assert s.findNumberOfLIS([1]) == 1

    assert s.findNumberOfLIS([2, 2, 2, 2, 2]) == 5

    assert s.findNumberOfLIS([84,-48,-33,-34,-52,72,75,-12,72,-45]) == 4