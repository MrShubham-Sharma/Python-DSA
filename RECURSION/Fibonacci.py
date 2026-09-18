class Solution:

            # we used the self because we're writting in the class so self must needed
    def func(self, num: int) -> int:
        # Base Case: If num is 0 or 1, return the number itself
        if num == 0 or num == 1:
            return num

        # Recursive Flow: sum of the previous two Fibonacci numbers
        return self.func(num - 1) + self.func(num - 2)
            # for calling the function in betwwen the class we required self.func()

    def fib(self, n: int) -> int:
        # Call the recursive function and return the result
        answer = self.func(n)
        print(answer)
        return answer

# in OOP we can give the direct call to function we must required to create an object or directory
object=Solution()
# then call bythis syntax obj.funct(n)
object.fib(6)