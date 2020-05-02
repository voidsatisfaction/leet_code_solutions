from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder_traverse(node: TreeNode, inorder_node_val_list: List[int]):
            if node is None:
                return

            inorder_traverse(node.left, inorder_node_val_list)
            inorder_node_val_list.append(node.val)
            inorder_traverse(node.right, inorder_node_val_list)

        inorder_node_val_list = []
        inorder_traverse(root, inorder_node_val_list)

        sorted_inorder_node_val_list = sorted(inorder_node_val_list)

        for i in range(1, len(inorder_node_val_list)):
            val1, val2 = sorted_inorder_node_val_list[i-1], sorted_inorder_node_val_list[i]

            if val1 == val2:
                return False


        for i in range(len(inorder_node_val_list)):
            val1, val2 = inorder_node_val_list[i], sorted_inorder_node_val_list[i]

            if val1 != val2:
                return False

        return True
