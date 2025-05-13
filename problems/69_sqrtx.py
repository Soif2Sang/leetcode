class Solution:
    def mySqrt(self, x: int) -> int:
        current_integer = 1
        while current_integer**2 <= x:
            current_integer += 1
        return current_integer - 1