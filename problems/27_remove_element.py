class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index_to_remove = []
        for i in range(len(nums)):
            if (nums[i] == val):
                index_to_remove.append(i)

        for index in index_to_remove[::-1]:
            nums.pop(index)

        return len(nums)
        