from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_length = len(nums)
        if num_length == 0:
            return 1

        has_last = False
        for i in range(num_length):
            while nums[i] >= 0 and nums[i] < num_length and nums[i] != i:
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp

                if nums[i] == nums[temp]:
                    break

            if nums[i] == num_length:
                has_last = True

        for i, n in enumerate(nums):
            if i == 0:
                continue
            if i != n:
                return i

        if has_last is False:
            return num_length

        return num_length+1

if __name__ == '__main__':
    s = Solution()

    assert s.firstMissingPositive([1,2,0]) == 3

    assert s.firstMissingPositive([3,4,-1,1]) == 2

    assert s.firstMissingPositive([7,8,9,11,12]) == 1

    assert s.firstMissingPositive([1, 1]) == 2


