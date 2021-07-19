from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = 0, 0, len(nums)-1

        while j <= k:
            if nums[j] == 2:
                self._swap(nums, j, k)
                k -= 1
            elif nums[j] == 1:
                j += 1
            else:
                self._swap(nums, i, j)
                i += 1
                j += 1

    def _swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
  s = Solution()

  nums = [2,0,2,1,1,0]
  s.sortColors(nums)
  assert nums == [0,0,1,1,2,2]

  nums = [2,0,1]
  s.sortColors(nums)
  assert nums == [0,1,2]

  nums = [0]
  s.sortColors(nums)
  assert nums == [0]

  nums = [1]
  s.sortColors(nums)
  assert nums == [1]