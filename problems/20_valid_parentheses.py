class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False

        open_stack = []
        close_stack = []

        binding = {
            '(': ')',
            '{': '}',
            '[': ']',
            ']': '[',
            ')': '(',
            '}': '{'
        }

        opening = ['(', '{', '[']
        closing = [')', '}', ']']

        for i in range(len(s)):
            element = s[i]

            # If the element is an opening bracket, we add it to the stack
            if element in opening:
                open_stack.append(element)

            # If the element is a closing bracket, we check if it matches the last opening bracket
            elif element in closing:
                # If the open stack is empty this means that we have a closing bracket without a opening bracket
                if not open_stack:
                    return False
                
                # If the last opening bracket is the same as the current closing bracket, we remove it from the open stack
                elif binding[element] == open_stack[-1]:
                    open_stack.pop()
                # If the last opening bracket is not the same as the current closing bracket, we return False
                else:
                    return False

        # If the stacks are empty, this means that all brackets are matched
        return len(open_stack) == 0 and len(close_stack) == 0 