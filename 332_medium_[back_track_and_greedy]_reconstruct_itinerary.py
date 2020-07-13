from typing import List, Dict, Tuple
from collections import defaultdict

class Solution:
    def _dfs(self, current_node: str, answer: List[str], ticket_num: int, adj_list: Dict, visited_edge_map: Dict) -> Tuple[bool, List[str]]:
        if len(answer) == ticket_num+1:
            return True, answer

        for adj_node in adj_list[current_node]:
            if visited_edge_map[current_node][adj_node] == 0:
                continue

            visited_edge_map[current_node][adj_node] -= 1
            answer.append(adj_node)

            finished, answer = self._dfs(adj_node, answer, ticket_num, adj_list, visited_edge_map)
            if finished is True:
                return finished, answer

            visited_edge_map[current_node][adj_node] += 1
            answer.pop()

        return False, answer


    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_num = len(tickets)
        tickets.sort(key=lambda ticket: ticket[1])

        adj_list = defaultdict(list)
        visited_edge_map = {}
        for ticket in tickets:
            start, end = ticket

            if start not in adj_list:
                visited_edge_map[start] = defaultdict(int)

            if len(adj_list[start]) == 0 or end != adj_list[start][-1]:
                adj_list[start].append(end)

            visited_edge_map[start][end] += 1

        _, answer = self._dfs('JFK', ['JFK'], ticket_num, adj_list, visited_edge_map)

        return answer

if __name__ == '__main__':
    s = Solution()
    assert s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"]

    assert s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"]

    assert s.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]) == ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]

