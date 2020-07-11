from typing import List

class Solution:
    def _is_reachable(self, hp: int, dungeon: List[List[int]]) -> bool:
        if hp <= 0:
            return False

        N, M = len(dungeon), len(dungeon[0])

        hp_map = [ [ 0 for _ in range(M) ] for _ in range(N) ]
        hp_map[0][0] = hp + dungeon[0][0]

        if hp_map[0][0] <= 0:
            return False

        for y in range(N):
            for x in range(M):
                if y == 0 and x == 0:
                    continue

                if y > 0 and hp_map[y-1][x] > 0:
                    hp_map[y][x] = max(hp_map[y][x], hp_map[y-1][x]+dungeon[y][x])

                if x > 0 and hp_map[y][x-1] > 0:
                    hp_map[y][x] = max(hp_map[y][x], hp_map[y][x-1]+dungeon[y][x])

        return hp_map[N-1][M-1] > 0

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        left, right = 1, 1

        N, M = len(dungeon), len(dungeon[0])
        for y in range(N):
            for x in range(M):
                if dungeon[y][x] < 0:
                    right -= dungeon[y][x]

        while left <= right:
            mid = (left + right) // 2

            if self._is_reachable(mid, dungeon) is True:
                if self._is_reachable(mid-1, dungeon) is False:
                    return mid

                right = mid-1
            else:
                left = mid+1
        
        return left

if __name__ == '__main__':
    s = Solution()

    print(s.calculateMinimumHP([[-200]]))
    # print(s.calculateMinimumHP([[-3, 5]]))
