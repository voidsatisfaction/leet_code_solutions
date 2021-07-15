from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS_list = [nums[0]]

        for i in range(1, len(nums)):
            num = nums[i]
            if num > LIS_list[-1]:
                LIS_list.append(num)
            else:
                index = self._binary_search(LIS_list, num)
                LIS_list[index] = num

        return len(LIS_list)

    def _binary_search(self, LIS_list: List[int], num: int) -> int:
        left, right = 0, len(LIS_list)-1

        while left < right:
            mid = (left+right) // 2

            if num == LIS_list[mid]:
                return mid

            if num > LIS_list[mid]:
                left = mid+1
            else:
                right = mid

        return left

if __name__ == '__main__':
    s = Solution()

    assert s.lengthOfLIS([1]) == 1

    assert s.lengthOfLIS([3,4,5,1]) == 3

    assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4

    assert s.lengthOfLIS([0,1,0,3,2,3]) == 4

    assert s.lengthOfLIS([7,7,7,7,7,7,7]) == 1
