from typing import List
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        level_val_lists = []

        tree_node_queue = Queue()
        tree_node_queue.put(root)

        while not tree_node_queue.empty():
            level_val_list = []

            level_node_nums = tree_node_queue.qsize()
            for _ in range(level_node_nums):
                tree_node = tree_node_queue.get()

                level_val_list.append(tree_node.val)

                if tree_node.left is not None:
                    tree_node_queue.put(tree_node.left)

                if tree_node.right is not None:
                    tree_node_queue.put(tree_node.right)

            level_val_lists.append(level_val_list)

        return level_val_lists
