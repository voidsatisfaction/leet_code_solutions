from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthLargestRec(nums, k, 0, len(nums)-1)

    def findKthLargestRec(self, nums: List[int], k: int, i: int, l: int) -> int:
        original_i = i
        original_l = l

        if i == l:
            return nums[i]

        if i == l-1:
            if k == 1:
                return max(nums[i], nums[l])
            if k == 2:
                return min(nums[i], nums[l])

        first, last, mid = nums[i], nums[l], nums[(i+l)//2]
        middle_value_element = sorted([first, last, mid])[1]
        if middle_value_element == last:
            self.swap(nums, i, l)
        elif middle_value_element == mid:
            self.swap(nums, i, (i+l)//2)

        j = i
        while j <= l:
            if nums[j] < nums[i]:
                self.swap(nums, i, j)
                i += 1
                j += 1
            elif nums[j] == nums[i]:
                self.swap(nums, i, j)
                j += 1
            else:
                self.swap(nums, j, l)
                l -= 1
    

        if original_l+1-k > l:
            return self.findKthLargestRec(nums, k, l+1, original_l)
        elif original_l+1-k >= i:
            return nums[i]
        else:
            return self.findKthLargestRec(nums, k-(original_l-i)-1, original_i, i-1)

    def swap(self, nums: List[int], i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i]

if __name__ == '__main__':
    s = Solution()
    assert s.findKthLargest([3,2,1,5,6,4], 2) == 5

    assert s.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

    assert s.findKthLargest([7,6,5,4,3,2,1], 5) == 3
