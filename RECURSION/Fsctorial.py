# flow 
# f(10)= 10*f(9*8*7...*1)

# base condition 
# if 10*(9*..*1)
# it means 10* f(10-1) =n*f(n-1) 
def my_function(n):
    if n==1:
        # if the the value calls n==1 it will stop 
        return 1
    return n*my_function(n-1)
x=my_function(10)
# define value for store
print(x)
# for visible output we assigned x to the function

# TC will be O(n)
# SC wil be O(n) in stack 