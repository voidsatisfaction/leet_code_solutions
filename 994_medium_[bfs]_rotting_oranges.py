from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        answer = self._bfs(grid)

        return answer

    def _bfs(self, grid: List[List[int]]) -> int:
        def get_all_next_coordinate(i: int, j: int, m: int, n: int) -> List[List[int]]:
            result = []
            direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for y, x in direction:
                next_y, next_x = i+y, j+x
                if next_y < 0 or next_y > m-1:
                    continue
                if next_x < 0 or next_x > n-1:
                    continue
                result.append([next_y, next_x])

            return result

        queue, m, n, phase = [], len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])

        while len(queue) > 0:
            next_queue = []
            for i, j in queue:
                next_coordinates = get_all_next_coordinate(i, j, m, n)

                for next_i, next_j in next_coordinates:
                    if grid[next_i][next_j] == 1:
                        grid[next_i][next_j] = 2
                        next_queue.append([next_i, next_j])
            
            if len(next_queue) == 0:
                break

            phase += 1
            queue = next_queue

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return phase

if __name__ == '__main__':
    s = Solution()

    assert s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4

    assert s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1

    assert s.orangesRotting([[0,2]]) == 0

    assert s.orangesRotting([[0]]) == 0