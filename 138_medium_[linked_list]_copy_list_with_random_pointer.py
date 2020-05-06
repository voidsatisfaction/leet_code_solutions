# Definition for a Node.
class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

# way1: destructive solution(modify old nodes)
class Solution:
    def copyRandomList(self, head: Node) -> Node:
        node = head
        new_head_node = new_node = Node(0)
        index_to_node_map = {}

        i = 0
        while node is not None:
            node.index = i

            new_node.next = Node(node.val)
            index_to_node_map[i] = new_node.next

            node = node.next
            new_node = new_node.next
            i += 1

        new_node = new_head_node.next
        node = head
        while node is not None:
            if node.random is None:
                node = node.next
                new_node = new_node.next
                continue

            random_index = node.random.index

            new_node.random = index_to_node_map[random_index]

            node = node.next
            new_node = new_node.next

        return new_head_node.next

# way2: Recursive solution without modification
class Solution:
    def copyRandomList(self, head: Node) -> Node:
        def copy_random_list_rec(old_node: Node):
            if old_node is None:
                return None

            if old_node in old_node_to_new_node_map:
                return old_node_to_new_node_map[old_node]

            new_node = Node(old_node.val)

            old_node_to_new_node_map[old_node] = new_node

            new_node.next = copy_random_list_rec(old_node.next)
            new_node.random = copy_random_list_rec(old_node.random)

            return new_node

        old_node_to_new_node_map = {}

        return copy_random_list_rec(head)

