from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = [ [] for _ in range(len(isConnected)) ]
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)

        num_province = 0
        visited = [ False for _ in range(len(isConnected)) ]
        for i in range(len(isConnected)):
            if visited[i] is False:
                num_province += 1
                self._dfs(i, visited, adj_list)

        return num_province

    def _dfs(self, i: int, visited: List[bool], adj_list: List[List[int]]) -> None:
        for adj_node in adj_list[i]:
            if visited[adj_node] is False:
                visited[adj_node] = True
                self._dfs(adj_node, visited, adj_list)


if __name__ == '__main__':
    s = Solution()

    assert s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2

    assert s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3

    assert s.findCircleNum([[1]]) == 1