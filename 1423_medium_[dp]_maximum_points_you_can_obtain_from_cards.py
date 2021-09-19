from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum_dp = [0]
        right_sum_dp = [0]

        for i in range(len(cardPoints)):
            left_card_point = cardPoints[i]
            right_card_point = cardPoints[-1-i]

            left_sum_dp.append(left_sum_dp[-1] + left_card_point)
            right_sum_dp.append(right_sum_dp[-1] + right_card_point)

        max_sum = -1
        for i in range(k+1):
            total_sum = left_sum_dp[i] + right_sum_dp[k-i]

            max_sum = max(max_sum, total_sum)

        return max_sum

if __name__ == '__main__':
    s = Solution()

    assert s.maxScore([1,2,3,4,5,6,1], 3) == 12

    assert s.maxScore([2,2,2], 2) == 4

    assert s.maxScore([9,7,7,9,7,7,9], 7) == 55

    assert s.maxScore([1, 1000, 1], 1) == 1

    assert s.maxScore([1,79,80,1,1,1,200,1], 3) == 202
