from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_cache = [nums[0]]
        sum_to_index_map = {}
        sum_to_index_map[nums[0]] = 0

        for i in range(1, len(nums)):
            sum_value = sum_cache[-1] + nums[i]

            sum_cache.append(sum_value)
            if sum_value not in sum_to_index_map:
                sum_to_index_map[sum_value] = i

        answer = 0
        for i in range(len(nums)-1, -1, -1):
            target_sum = - (k - sum_cache[i])

            if target_sum == 0:
                answer = max(answer, i+1)

            if sum_to_index_map.get(target_sum) is not None:
                answer = max(answer, i-sum_to_index_map[target_sum])

        return answer

if __name__ == '__main__':
    s = Solution()

    assert s.maxSubArrayLen([1,-1,5,-2,3], 3) == 4

    assert s.maxSubArrayLen([-2,-1,2,1], 1) == 2
