from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def get_max_subarray_product(start: int, end: int) -> int:
            if start > end:
                return 0

            if start == end:
                return nums[start]

            total_product = 1
            for i in range(start, end+1):
                total_product *= nums[i]

            if total_product > 0:
                return total_product
            
            product_until_first_minus = 1
            for i in range(start, end+1):
                product_until_first_minus *= nums[i]
                if nums[i] < 0:
                    break

            proudct_until_first_minus_backward = 1
            for i in reversed(range(start, end+1)):
                proudct_until_first_minus_backward *= nums[i]
                if nums[i] < 0:
                    break

            return int(max(
                total_product / product_until_first_minus,
                total_product / proudct_until_first_minus_backward
            ))

        start, end = 0, 0

        nums_length = len(nums)

        max_subarray_product = nums[start]

        while end <= nums_length:
            if end == nums_length or nums[end] == 0:
                max_subarray_product_candidate = get_max_subarray_product(start, end-1)
                max_subarray_product = max(max_subarray_product, max_subarray_product_candidate)

                if end == nums_length:
                    break

                max_subarray_product = max(max_subarray_product, 0)
                start, end = end+1, end+1

            else:
                end += 1

        return max_subarray_product

if __name__ == '__main__':
    print(Solution().maxProduct([2, 3, -2, 4]))
    print(Solution().maxProduct([0]))
    print(Solution().maxProduct([0, 0]))
    print(Solution().maxProduct([0, 0, 0, 1]))
    print(Solution().maxProduct([-2, 0, -1]))