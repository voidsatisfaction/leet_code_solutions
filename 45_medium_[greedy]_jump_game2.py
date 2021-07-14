from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        max_jump_index_list = [ i+num for i, num in enumerate(nums) ]

        i, j, max_index, phase = 0, 0, nums[0], 0
        while j < len(nums)-1:
            j = max_index
            while i <= j and i < len(nums):
                max_index = max(max_index, max_jump_index_list[i])
                i += 1
            phase += 1

        return phase

if __name__ == '__main__':
    s = Solution()

    assert s.jump([2]) == 0

    assert s.jump([2,1]) == 1

    assert s.jump([2, 3, 1, 1, 4]) == 2

    assert s.jump([2, 3, 0, 1, 4]) == 2