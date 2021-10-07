from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def is_flip_equivalent_rec(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 is None and node2 is None:
                return True
            elif node1 is None:
                return False
            elif node2 is None:
                return False

            if node1.val != node2.val:
                return False

            return (is_flip_equivalent_rec(node1.left, node2.left) and \
                is_flip_equivalent_rec(node1.right, node2.right)) or \
                    (is_flip_equivalent_rec(node1.left, node2.right) and \
                is_flip_equivalent_rec(node1.right, node2.left))

        result = is_flip_equivalent_rec(root1, root2)

        return result

