# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.inorderTraversal(p) == self.inorderTraversal(q)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        memory = []

        self.inorderTraversalWithMemory(root, memory, 'R')

        return memory

    def inorderTraversalWithMemory(self, root, memory, place):
        if root is None:
            return

        self.inorderTraversalWithMemory(root.left, memory, 'L')
        memory.append(root.val)
        memory.append(place)
        self.inorderTraversalWithMemory(root.right, memory, 'R')
