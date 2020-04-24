from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        if n == 0 or n == 1:
            return

        i = 0
        original_n_index = n-1
        while n > 0:
            left_top = (i, i)
            right_top = (i, original_n_index-i)
            right_bottom = (original_n_index-i, original_n_index-i)
            left_bottom = (original_n_index-i, i)
            for _ in range(n-1):
                lty, ltx = left_top
                rty, rtx = right_top
                rby, rbx = right_bottom
                lby, lbx = left_bottom

                matrix[rty][rtx], matrix[rby][rbx], matrix[lby][lbx], matrix[lty][ltx] = \
                    matrix[lty][ltx], matrix[rty][rtx], matrix[rby][rbx], matrix[lby][lbx]

                left_top = (lty, ltx+1)
                right_top = (rty+1, rtx)
                right_bottom = (rby, rbx-1)
                left_bottom = (lby-1, lbx)

            n -= 2
            i += 1
        

if __name__ == '__main__':
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    Solution().rotate(matrix)

    matrix = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
    Solution().rotate(matrix)
    print(matrix)

    print(matrix[::-1])
    print(1, ~1, ~3)