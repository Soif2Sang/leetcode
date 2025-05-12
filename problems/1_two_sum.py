class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for y in range(i, len(nums)):
                if i == y:
                    continue

                if (nums[i] + nums[y]) == target:
                    return [i,y]
                