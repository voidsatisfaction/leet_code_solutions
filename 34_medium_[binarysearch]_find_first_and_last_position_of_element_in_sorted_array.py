from typing import List

class Solution:
    def _search_lowest_target_index(self, nums: List[int], target: int) -> int:
        lowest_index = 0

        low, high = 0, len(nums)-1
        while low <= high:
            mid = int((low + high)/2)

            if nums[mid] == target:
                if mid == 0:
                    return 0
                elif nums[mid-1] == target:
                    high = mid-1
                else:
                    return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1

        return -1

    def _search_highest_target_index(self, nums: List[int], target: int) -> int:
        highest_index = 0

        low, high = 0, len(nums)-1
        while low <= high:
            mid = int((low+high)/2)

            if nums[mid] == target:
                if mid == len(nums)-1:
                    return len(nums)-1
                elif nums[mid+1] == target:
                    low = mid+1
                else:
                    return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        lowest_index, highest_index = self._search_lowest_target_index(nums, target), self._search_highest_target_index(nums, target)

        return [lowest_index, highest_index]

        
if __name__ == '__main__':
    print(Solution().searchRange([5,7,7,8,8,10], 8))
    print(Solution().searchRange([5,7,7,8,8,10], 11))
    print(Solution().searchRange([5,7,7,8,8,10], 7))
    print(Solution().searchRange([5,7,7,8,8,10], 5))
    print(Solution().searchRange([2, 2], 2))
    print(Solution().searchRange([2], 2))
    print(Solution().searchRange([2], 0))