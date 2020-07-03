from typing import List

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# way1: bfs with stack
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        stack = [root]
        answer = []

        from_left = True

        while len(stack) > 0:
            buffer_stack = []
            current_level_answer = []

            while len(stack) > 0:
                node = stack.pop()

                current_level_answer.append(node.val)

                if from_left is True:
                    if node.left is not None:
                        buffer_stack.append(node.left)
                    if node.right is not None:
                        buffer_stack.append(node.right)
                else:
                    if node.right is not None:
                        buffer_stack.append(node.right)
                    if node.left is not None:
                        buffer_stack.append(node.left)

            from_left = not from_left

            answer.append(current_level_answer)

            stack = buffer_stack

        return answer

# way2: dfs
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(node: TreeNode, level: int, answer) -> None:
            if level >= len(answer):
                answer.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    answer[level].append(node.val)
                else:
                    answer[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node is not None:
                    dfs(next_node, level+1, answer)

        if root is None:
            return []

        answer = []

        dfs(root, 0, answer)

        return answer


