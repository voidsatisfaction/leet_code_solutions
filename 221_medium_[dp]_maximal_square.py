from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def get_largest_size_of_square(row, column, row_max_index, column_max_index):
            size = int(matrix[row][column])

            if size == 0:
                return size

            while True:
                size += 1

                if column+size-1 > column_max_index or row+size-1 > row_max_index:
                    return size-1

                for i in range(row, row+size):
                    if i > row_max_index or matrix[i][column+size-1] == '0':
                        return size-1

                for j in range(column, column+size):
                    if j > column_max_index or matrix[row+size-1][j] == '0':
                        return size-1

        def update_matrix_size(row, column, size):
            if size == 0:
                return

            s = 1
            while size > 0:
                for i in range(row, row+s):
                    matrix[i][column+s-1] = size

                for j in range(column, column+s):
                    matrix[row+s-1][j] = size

                s += 1
                size -= 1
                

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        max_row_index = len(matrix)-1
        max_column_index = len(matrix[0])-1

        max_size = 0

        for row in range(max_row_index+1):
            for column in range(max_column_index+1):
                size = get_largest_size_of_square(row, column, max_row_index, max_column_index)
                update_matrix_size(row, column, size)

                max_size = max(max_size, size)
        
        return max_size * max_size

if __name__ == '__main__':
    print(Solution().maximalSquare([
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '1', '1', '1']
    ]))

    print(Solution().maximalSquare([['1']]))
    print(Solution().maximalSquare([['0']]))
