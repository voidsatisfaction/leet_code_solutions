from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0:
            return

        self._reverse(nums, 0, len(nums)-1)
        self._reverse(nums, 0, k-1)
        self._reverse(nums, k, len(nums)-1)

    def _reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            self._swap(nums, start, end)

            start += 1
            end -= 1

    def _swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    s = Solution()

    nums = [1]
    s.rotate(nums, 100)
    assert nums == [1]

    nums = [1,3]
    s.rotate(nums, 0)
    assert nums == [1,3]

    nums = [1,2,3]
    s.rotate(nums, 2)
    assert nums == [2,3,1]

    nums = [1,2,3,4,5,6,7]
    s.rotate(nums, 3)
    assert nums == [5,6,7,1,2,3,4]

    nums = [-1,-100,3,99]
    s.rotate(nums, 2)
    assert nums == [3,99,-1,-100]