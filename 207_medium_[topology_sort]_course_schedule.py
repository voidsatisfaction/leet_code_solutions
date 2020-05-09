from typing import List
from queue import Queue

class Node:
    def __init__(self, index, next_node_list, before_node_num=0):
        self.index = index
        self.next_node_list = next_node_list
        self.before_node_num = before_node_num

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_list = [ Node(i, []) for i in range(numCourses) ]

        for prerequisite in prerequisites:
            next_node_index = prerequisite[0]
            before_node_index = prerequisite[1]

            next_node = node_list[next_node_index]
            next_node.before_node_num += 1

            node_list[before_node_index].next_node_list.append(next_node)

        traversed_node_num = 0

        q = Queue()

        for node in node_list:
            if node.before_node_num == 0:
                traversed_node_num += 1
                q.put(node)

        while q.qsize() > 0:
            node = q.get()

            for next_node in node.next_node_list:
                next_node.before_node_num -= 1

                if next_node.before_node_num == 0:
                    traversed_node_num += 1
                    q.put(next_node)

        return traversed_node_num == numCourses

if __name__ == '__main__':
    print(Solution().canFinish(2, [[1,0]]))
    print(Solution().canFinish(2, [[1,0], [0,1]]))
    print(Solution().canFinish(1, []))
    print(Solution().canFinish(1, [[0,0]]))