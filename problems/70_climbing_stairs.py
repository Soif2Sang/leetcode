#To be fair, I did NOT find myself that it was fibonacci, I had to check the comments section.

fibonacci_cache = {1: 1, 2: 2}

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n):
            if n==1:
                return 1

            if n ==2:
                return 2
            
            if n-1 not in fibonacci_cache:
                fibonacci_cache[n-1] = climb(n-1)

            if n-2 not in fibonacci_cache:
                fibonacci_cache[n-2] = climb(n-2)

            return fibonacci_cache[n-1] + fibonacci_cache[n-2]

        return climb(n)