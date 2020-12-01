from typing import List

class DisjointSet:
    def __init__(self, n: int, N: int, M: int) -> None:
        self._forest = [-1 for _ in range(n)]
        self._size_list = [1 for _ in range(n)]
        self._entire_island_num = 0

        self._N = N
        self._M = M

    def add_num(self, n: int, up: int, down: int, left: int, right: int) -> int:
        if self._forest[n] != -1:
            return self._entire_island_num
        # place new island
        self._forest[n] = n

        # query four places
        up_root = self._root(up)
        down_root = self._root(down)
        left_root = self._root(left)
        right_root = self._root(right)

        if up_root == -1 and down_root == -1 and left_root == -1 and right_root == -1:
            self._entire_island_num += 1

            return self._entire_island_num

        s = set([up_root, down_root, left_root, right_root])
        if -1 in s:
            s.remove(-1)
        distinct_root_n = len(s)

        self._entire_island_num -= (distinct_root_n-1)

        # merge four places
        self.merge(n, up)
        self.merge(n, down)
        self.merge(n, left)
        self.merge(n, right)

        return self._entire_island_num

    def merge(self, n: int, m: int) -> None:
        n_root = self._root(n)
        m_root = self._root(m)

        if n_root == m_root or n_root == -1 or m_root == -1:
            return

        if self._size_list[n_root] >= self._size_list[m_root]:
            self._forest[m_root] = n_root
            self._size_list[n_root] += self._size_list[m_root]
        else:
            self._forest[n_root] = m_root
            self._size_list[m_root] += self._size_list[n_root]

    def _root(self, n: int) -> int:
        if n < 0 or n >= self._M * self._N or self._forest[n] == -1:
            return -1

        original_n = n

        while n != self._forest[n]:
            n = self._forest[n]

        root_n = n
        self._forest[original_n] = root_n

        return n

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        n, m = m, n
        ds = DisjointSet(n*m, n, m)

        ans_list = []

        for position in positions:
            [i, j] = position

            converted_n = i*m + j

            up = -1 if i == 0 else converted_n-m
            down = -1 if i == n-1 else converted_n+m
            left = -1 if j == 0 else converted_n-1
            right = -1 if j == m-1 else converted_n+1

            ans = ds.add_num(
                converted_n,
                up,
                down,
                left,
                right
            )

            ans_list.append(ans)

        return ans_list

if __name__ == '__main__':
    s = Solution()
    assert s.numIslands2(3, 3, [[0,0], [0,1], [1,2], [2,1]]) == [1,1,2,3]
    assert s.numIslands2(1, 2, [[0,1],[0,0]]) == [1,1]
    assert s.numIslands2(8, 2, [[7,0]]) == [1]