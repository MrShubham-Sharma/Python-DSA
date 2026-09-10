# print X at N times
# we take an parameters not using an count just x & n
def my_funct(x,n):
    # if we want the print x till 5 times it will 
    # needs the parameters so we need also stop the pogram so we 
    # just return the value to stop
    if n==0:
        return
    print(x)
    # x will counter where once the code is run for n times it will catch the 
    # count as 4-1 =5 
    my_funct(x,n-1)
# we give an values to function
my_funct("Hello",5)

# print 1 to N using Recursion
def my_funct(i,n):

    # so here we go with i we need to print till N so we need n must be grater 
    if i>n:
        return
    print(i)
    # here we need to add i +1 means 1+1=2 till 4
    my_funct(i+1,n)
my_funct(1,4)

# Tail Recursion
def my_funct(x,n):
    if x>n:
        return
    # in Tail recursion as usual we write an logic first and then the output
    my_funct(x+1,n)
    # at first the counter will execute till N then the output will print Nth times
    print(x)
my_funct(1,9)

# it aslo called as backtracking where the it will end-up on the 1+1=2 amd n=9,9,9 
# so after thatnit will start printing from 9-1 
# because the logic execute first and printing later 