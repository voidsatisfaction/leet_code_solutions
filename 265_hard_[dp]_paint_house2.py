from collections import deque
from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0

        n, k = len(costs), len(costs[0])

        converted_costs = costs
        converted_dp_costs = [[None for _ in range(k)] for _ in range(n)]

        for i in range(n):
            for j in range(k):
                converted_dp_costs[i][j] = costs[i][j]

        for i in range(1, n):
            d = deque()
            for j, cost in enumerate(converted_dp_costs[i-1]):
                if len(d) == 0:
                    d.append((cost, j))
                elif len(d) == 1:
                    minimum_cost, _ = d[0]
                    if cost < minimum_cost:
                        d.appendleft((cost, j))
                    else:
                        d.append((cost, j))
                else:
                    minimum_cost, _ = d[0]
                    second_minimum_cost, _ = d[1]
                    if cost < minimum_cost:
                        d.pop()
                        d.appendleft((cost, j))
                    elif cost < second_minimum_cost:
                        d.pop()
                        d.append((cost, j))

            minimum_cost, minimum_cost_index = d[0]
            second_minimum_cost, second_minimum_cost_index = d[1]
            for j in range(k):
                if minimum_cost_index != j:
                    converted_dp_costs[i][j] = minimum_cost + converted_costs[i][j]
                else:
                    converted_dp_costs[i][j] = second_minimum_cost + converted_costs[i][j]

        return min(converted_dp_costs[n-1])

if __name__ == '__main__':
    s = Solution()
    assert s.minCostII([[1,5,3],[2,9,4]]) == 5
    assert s.minCostII([[2, 5, 100, 20]]) == 2