from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(sorted_num_list: List[int], target: int) -> bool:
            left, right = 0, len(sorted_num_list)-1

            while left <= right:
                mid = int((left+right)/2)

                mid_val = sorted_num_list[mid]

                if mid_val == target:
                    return True
                elif target > mid_val:
                    left = mid+1
                else:
                    right = mid-1

            return False

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        n= len(matrix)

        for row in range(n):
            if matrix[row][0] > target:
                break

            sorted_num_list = matrix[row]

            if binary_search(sorted_num_list, target):
                return True

        return False

if __name__ == '__main__':
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    assert Solution().searchMatrix(matrix, 5) is True
    assert Solution().searchMatrix(matrix, 20) is False

    matrix = []

    assert Solution().searchMatrix(matrix, 5) is False

    matrix = [[]]

    assert Solution().searchMatrix(matrix, 5) is False

    matrix = [[5]]

    assert Solution().searchMatrix(matrix, 5) is True

