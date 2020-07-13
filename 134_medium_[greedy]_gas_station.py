from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        index_list = []
        gas_and_cost = zip(gas, cost)

        prev_gas_cost_diff = -1
        for i, (gas_val, cost_val) in enumerate(gas_and_cost):
            current_gas_cost_diff = gas_val - cost_val

            if current_gas_cost_diff >= 0 and prev_gas_cost_diff < 0:
                index_list.append(i)

            prev_gas_cost_diff = current_gas_cost_diff

        def dfs(current_index: int, start_index: int, gas_cost_diff_state: int) -> int:
            if gas_cost_diff_state < 0:
                return -1

            if current_index != start_index and current_index%len(gas) == start_index:
                return start_index

            current_gas_cost_diff = gas[current_index%len(gas)] - cost[current_index%len(gas)]

            return dfs(
                current_index+1,
                start_index,
                gas_cost_diff_state+current_gas_cost_diff
            )

        for i in index_list:
            result = dfs(i, i, 0)
            if result >= 0:
                return result

        return -1

if __name__ == '__main__':
    s = Solution()

    assert s.canCompleteCircuit(
        [1,2,3,4,5],
        [3,4,5,1,2]
    ) == 3

    assert s.canCompleteCircuit(
        [2,3,4],
        [3,4,3]
    ) == -1