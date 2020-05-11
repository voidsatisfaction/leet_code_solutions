# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node: TreeNode, path: str, target_node1: TreeNode, target_node2: TreeNode):
            if node is None:
                return

            if node.val == target_node1.val:
                target_paths[0] = path
            
            if node.val == target_node2.val:
                target_paths[1] = path

            dfs(node.left, path + 'l', target_node1, target_node2)
            dfs(node.right, path + 'r', target_node1, target_node2)
        
        target_paths = ['', '']
        dfs(root, '', p, q)
        
        target_path1 = target_paths[0]
        target_path2 = target_paths[1]

        common_path = ''
        for i in range(min(len(target_path1), len(target_path2))):
            if target_path1[i] == target_path2[i]:
                common_path += target_path1[i]
            else:
                break
                
        
        if len(common_path) == 0:
            return root

        node = root
        for c in common_path:
            if c == 'l':
                node = node.left
            elif c == 'r':
                node = node.right

        return node

        