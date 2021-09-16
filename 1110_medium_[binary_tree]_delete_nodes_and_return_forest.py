from typing import List, Set

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def make_forest_rec(node: TreeNode, delete_flag: bool, to_delete_set: Set[int], answer: List[TreeNode]) -> None:
            if node.left is not None:
                if node.left.val in to_delete_set:
                    temp = node.left
                    node.left = None
                    make_forest_rec(temp, True, to_delete_set, answer)
                else:
                    if delete_flag is True:
                        answer.append(node.left)
                    make_forest_rec(node.left, False, to_delete_set, answer)

            if node.right is not None:
                if node.right.val in to_delete_set:
                    temp = node.right
                    node.right = None
                    make_forest_rec(temp, True, to_delete_set, answer)
                else:
                    if delete_flag is True:
                        answer.append(node.right)
                    make_forest_rec(node.right, False, to_delete_set, answer)

        to_delete_set = set(to_delete)
        answer = []

        if root.val in to_delete_set:
            make_forest_rec(root, True, to_delete_set, answer)
        else:
            answer.append(root)
            make_forest_rec(root, False, to_delete_set, answer)

        return answer
