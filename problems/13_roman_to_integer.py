mapping = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        was_substracted = False
        for i in range(len(s)):
            # If the previous roman letter was used as a substractor, we pass this time because it has already been computed
            if was_substracted:
                was_substracted = False
                continue

            is_last_index = i != (len(s) -1)

            if is_last_index and s[i] == 'I' and s[i+1] in ['V', 'X']:
                was_substracted = True  
                total += mapping[s[i+1]] - mapping['I']

            elif is_last_index and s[i] == 'X' and s[i+1] in ['L', 'C']:
                was_substracted = True  
                total += mapping[s[i+1]] - mapping['X']

            elif is_last_index and s[i] == 'C' and s[i+1] in ['D', 'M']:
                was_substracted = True
                total += mapping[s[i+1]] - mapping['C']

            else:
                total += mapping[s[i]]
                was_substracted = False
                
        return total