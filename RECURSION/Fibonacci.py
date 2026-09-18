class Solution:

    def func(self, num: int) -> int:
        # Base Case: If num is 0 or 1, return the number itself
        if num == 0 or num == 1:
            return num

        # Recursive Flow: sum of the previous two Fibonacci numbers
        return self.func(num - 1) + self.func(num - 2)

    def fib(self, n: int) -> int:
        # Call the recursive function and return the result
        answer = self.func(n)
        return answer