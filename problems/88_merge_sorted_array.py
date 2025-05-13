class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print("Start:", nums1, m, nums2, n)
        nums1 = nums1[:m]
        nums2 = nums2[:n]
        print("Reduced:", nums1, nums2)

        if not nums1:
            return nums2
        if not nums2:
            return nums1
        
        if not nums1 and not nums2:
            return []

        for number in nums2:
            print("before", nums1)
            nums1 = self.addNumberToList(nums1, number)
            print("result", nums1)

        print("ici", nums1)
        return nums1
    
    def addNumberToList(self, nums1, number):
        """
        This function aims to add a number to a sorted linked list
        """
        print("Adding", number)
        if nums1[0] > number:
            nums1.insert(0, number)
            return nums1

        for i in range(len(nums1)):
            print("current number", nums1[i])
            if nums1[i] >= number:
                nums1.insert(i, number)
                return nums1

        
        nums1.append(number)

        return nums1