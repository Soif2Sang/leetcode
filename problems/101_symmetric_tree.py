# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.leftInOrder(root.left) == self.RightInOrder(root.right)

    def leftInOrder(self, root: Optional[TreeNode]) -> List[int]:
        memory = []

        self.leftInOrderWithMemory(root, memory, 'R')

        return memory

    def leftInOrderWithMemory(self, root, memory, place):
        if root is None:
            return

        self.leftInOrderWithMemory(root.left, memory, 'L')
        memory.append(root.val)
        memory.append(place)
        self.leftInOrderWithMemory(root.right, memory, 'R')

    def RightInOrder(self, root: Optional[TreeNode]) -> List[int]:
        memory = []

        self.RightInOrderWithMemory(root, memory, 'R')

        return memory

    def RightInOrderWithMemory(self, root, memory, place):
        if root is None:
            return

        # When checking for symmetry, the left and right subtrees are mirrored. Thus, in the right inorder traversal, 'L' becomes 'R' and vice versa.
        # Consequently, RightInOrderWithMemory processes the right child with 'L' and the left child with 'R'.
        self.RightInOrderWithMemory(root.right, memory, 'L')
        memory.append(root.val)
        memory.append(place)
        self.RightInOrderWithMemory(root.left, memory, 'R')