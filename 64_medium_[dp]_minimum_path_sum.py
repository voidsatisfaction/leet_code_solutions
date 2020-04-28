import math
from typing import List
from queue import Queue

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        dp = [[ math.inf for j in range(m) ] for i in range(n) ]

        q = Queue()
        q.put((0, 0))
        dp[0][0] = grid[0][0]

        pos = [(1, 0), (0, 1)]

        while not q.empty():
            original_y, original_x = q.get()
            for p in pos:
                y = original_y + p[0]
                x = original_x + p[1]

                if y > n-1 or x > m-1:
                    continue

                if dp[y][x] == math.inf:
                    q.put((y, x))
                
                dp[y][x] = min(
                    dp[y][x],
                    grid[y][x] + dp[original_y][original_x]
                )

        return dp[n-1][m-1]

if __name__ == '__main__':
    print(Solution().minPathSum([
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]))
    print(Solution().minPathSum([
        [1]
    ]))
    print(Solution().minPathSum(
        [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]

    ))