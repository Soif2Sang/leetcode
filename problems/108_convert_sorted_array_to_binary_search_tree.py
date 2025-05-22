# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root_value = nums[len(nums) // 2]
        left_sequence = nums[:len(nums) // 2]
        right_sequence = nums[len(nums) // 2 +1:]


        root = TreeNode(root_value, None, None)
        root.left = self.sortedArrayToBST(left_sequence)
        root.right = self.sortedArrayToBST(right_sequence)

        return root