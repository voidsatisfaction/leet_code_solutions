from typing import Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    def __init__(self, root: TreeNode):
        def get_level_and_index(root: TreeNode) -> Tuple[int, int]:
            def get_node_number(root: TreeNode) -> int:
                if root is None:
                    return 0

                left_subtree_node_number = get_node_number(root.left)
                right_subtree_node_number = get_node_number(root.right)

                return left_subtree_node_number + right_subtree_node_number + 1

            total_node_number = n = get_node_number(root)
            level = -1
            
            while n > 0:
                level += 1
                n //= 2

            return level, total_node_number - 2**level

        self._root = root
        self._level, self._index = get_level_and_index(root)

        self._update_index_and_level()

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)

        level_index_binary = self._get_level_index_to_binary()

        parent_node, current_node = self._root, self._root
        for c in level_index_binary:
            parent_node = current_node
            if c == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

        if level_index_binary[-1] == '0':
            parent_node.left = new_node
        else:
            parent_node.right = new_node

        self._update_index_and_level()

        return parent_node.val
        

    def get_root(self) -> TreeNode:
        return self._root

    def _get_level_index_to_binary(self) -> str:
        return bin(self._index)[2:].zfill(self._level)

    def _update_index_and_level(self) -> None:
        self._index += 1
        if self._index == 2**(self._level):
            self._level += 1
            self._index = 0



# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()