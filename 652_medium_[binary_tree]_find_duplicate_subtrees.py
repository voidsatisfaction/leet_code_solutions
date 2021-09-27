from collections import defaultdict
from typing import List, Optional, DefaultDict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def post_order_traversal(
            node: Optional[TreeNode],
            key_to_visit_count_map: DefaultDict[str, int],
            answer: List[TreeNode]
        ) -> str:
            if node is None:
                return 'x'

            left_key = post_order_traversal(node.left, key_to_visit_count_map, answer)
            right_key = post_order_traversal(node.right, key_to_visit_count_map, answer)

            current_key = f'{node.val}l{left_key}r{right_key}'

            key_to_visit_count_map[current_key] += 1

            if current_key in key_to_visit_count_map and key_to_visit_count_map[current_key] == 2:
                answer.append(node)

            return current_key

        key_to_visit_count_map = defaultdict(int)
        answer = []

        post_order_traversal(root, key_to_visit_count_map, answer)

        return answer