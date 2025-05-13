class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for letter in s[::-1]:
            if letter != " ":
                count += 1
            elif count != 0:
                return count
        return count