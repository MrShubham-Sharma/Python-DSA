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