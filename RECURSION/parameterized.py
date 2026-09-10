# Parameterized Recursion
# Sum of 1 to N 
def My_funct(sum,i,n):
    if i >n:
        # n is an limit counter where we need to stop if num>limit
        print(sum)
        # sum will count the addition 
        return
    My_funct(sum+i,i+1,n)
    # sum = 0+1 initial phase, 1+1 addition counter ,n>5 limiter ?
My_funct(0,1,5)
