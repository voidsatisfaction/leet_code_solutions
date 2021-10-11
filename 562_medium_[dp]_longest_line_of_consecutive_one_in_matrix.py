from typing import List

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [ [ [ 0 for _ in range(4) ] for _ in range(n) ] for _ in range(m) ]

        answer = 0
        for row in range(m):
            for column in range(n):
                if mat[row][column] == 0:
                    continue

                for direction in range(4):
                    if direction == 0: # horizontal
                        if column == 0:
                            value = 1
                        else:
                            value = dp[row][column-1][direction] + 1
                    elif direction == 1: # vertical
                        if row == 0:
                            value = 1
                        else:
                            value = dp[row-1][column][direction] + 1
                    elif direction == 2: # diagonal
                        if row == 0 or column == 0:
                            value = 1
                        else:
                            value = dp[row-1][column-1][direction] + 1
                    else: # antidiagonal
                        if row == 0 or column == n-1:
                            value = 1
                        else:
                            value = dp[row-1][column+1][direction] + 1

                    dp[row][column][direction] = value
                    answer = max(answer, dp[row][column][direction])

        return answer


if __name__ == '__main__':
    s = Solution()

    assert s.longestLine([[0,1,1,0],[0,1,1,0],[0,0,0,1]]) == 3
    assert s.longestLine([[1,1,1,1],[0,1,1,0],[0,0,0,1]]) == 4