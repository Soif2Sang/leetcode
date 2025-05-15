# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        memory = []

        self.inorderTraversalWithMemory(root, memory)

        return memory

    def inorderTraversalWithMemory(self, root, memory):
        if root is None:
            return

        self.inorderTraversalWithMemory(root.left, memory)
        memory.append(root.val)
        self.inorderTraversalWithMemory(root.right, memory)
