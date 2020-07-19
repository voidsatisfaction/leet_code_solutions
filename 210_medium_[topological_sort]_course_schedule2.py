from typing import List
from collections import defaultdict, deque

class Node:
    def __init__(self, num: int, before_count=0):
        self.num = num
        self.before_count = before_count

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]

        num_node_mapper = [ Node(i) for i in range(numCourses) ]
        adj_set = defaultdict(set)

        for (node_num2, node_num1) in prerequisites:
            adj_set[node_num1].add(node_num2)
            num_node_mapper[node_num2].before_count += 1

        q = deque()
        for i in range(numCourses):
            node = num_node_mapper[i]
            if node.before_count == 0:
                q.append(node)

        answer = []
        while len(q) > 0:
            node = q.popleft()
            answer.append(node.num)

            to_be_removed = []
            for adj_node_num in adj_set[node.num]:
                adj_node = num_node_mapper[adj_node_num]
                adj_node.before_count -= 1
                if adj_node.before_count == 0:
                    q.append(adj_node)
                    to_be_removed.append(adj_node_num)

            for adj_node_num in to_be_removed:
                adj_set[node.num].remove(adj_node_num)

        if len(answer) == numCourses:
            return answer

        return []

if __name__ == '__main__':
    s = Solution()

    assert s.findOrder(2, [[1,0]]) == [0,1]

    assert s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,1,2,3] or s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,2,1,3]

    assert s.findOrder(1, [[]]) == [0]

    assert s.findOrder(2, [[0, 1], [1, 0]]) == []

    assert s.findOrder(2, []) == [0, 1] or s.findOrder(2, []) == [1, 0]