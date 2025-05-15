class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        best_prefix = ""
        current_prefix = ""

        for i in range(len(min(strs))):
            for y in range(len(strs)):
                if strs[y] == "":
                    return ""
                print("Current word", y,strs[y])
                if y == 0:
                    print("Adding a new letter to the streak", y,i, strs[y][i])
                    current_prefix += strs[y][i]
                elif current_prefix[-1] != strs[y][i]:
                    print("It broke the record")
                    return best_prefix
            
            best_prefix = current_prefix
            print("New streak updated", best_prefix)
        return best_prefix