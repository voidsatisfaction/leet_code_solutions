from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        y, x = 0, 0

        answer = []
        while x < n:
            initial_x = x
            is_stuck = False

            while y < m:
                if grid[y][x] == 1:
                    if x == n-1 or grid[y][x+1] == -1:
                        is_stuck = True
                        break
                    
                    x += 1
                else:
                    if x == 0 or grid[y][x-1] == 1:
                        is_stuck = True
                        break

                    x -= 1

                y += 1

            if is_stuck:
                answer.append(-1)
            else:
                answer.append(x)

            y = 0
            x = initial_x + 1

        return answer


if __name__ == '__main__':
    s = Solution()

    assert s.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]) == [1,-1,-1,-1,-1]

    assert s.findBall([[-1]]) == [-1]

    assert s.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]) == [0,1,2,3,4,-1]
