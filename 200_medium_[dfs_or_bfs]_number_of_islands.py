class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int, visited: List[List[bool]]) -> None:
            if i < 0 or j < 0 or i >= N or j >= M or grid[i][j] == "0" or visited[i][j]:
                return

            visited[i][j] = True

            positions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            for pos in positions:
                neighbor_i = i + pos[0]
                neighbor_j = j + pos[1]

                dfs(neighbor_i, neighbor_j, visited)

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        N, M = len(grid), len(grid[0])

        visited = [ [ False for _ in range(M) ] for _ in range(N) ]

        island_num = 0

        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1" and not visited[i][j]:
                    island_num += 1
                    dfs(i, j, visited)

        return island_num

