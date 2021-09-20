from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        current_sum = nums[0]
        min_length = MIN_LENGTH = 10**5+1

        while i < len(nums):
            if current_sum < target:
                i += 1
                if i == len(nums):
                    break
                current_sum += nums[i]
            else:
                min_length = min(min_length, i-j+1)
                j += 1
                current_sum -= nums[j-1]

        if min_length == MIN_LENGTH:
            return 0

        return min_length


if __name__ == '__main__':
    s = Solution()

    assert s.minSubArrayLen(7, [2,3,1,2,4,3]) == 2

    assert s.minSubArrayLen(4, [1,4,4]) == 1

    assert s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0

    assert s.minSubArrayLen(11, [1,2,3,4,5]) == 3