# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left, right = self.dfs(root.left), self.dfs(root.right)
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), left + right)

    def dfs(self, root):
        if not root:
            return 0
        res = 1+max(self.dfs(root.left), self.dfs(root.right))
        return res        