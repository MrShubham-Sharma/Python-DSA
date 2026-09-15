# normal Recursion for sum of 1-N
def my_funct(sum,i,n):
    if i >n:
        # it will stop at where i > n 
        print(sum)
        return
    my_funct(sum+i,i+1,n)
    # it runs the logic where the sum will add up the i 1+2+3+4+5 and
    # i will goes like 1,2,3 and n will be the limiter
my_funct(0,1,14)

# in the functional recursion we not requierd to print we need to return somthing 
# we do not need to call function we're returning the output

# Create logic Flow 

# for 10 to 1 
# f(10)=10+f(9+8+7...1)
    # 9+f(8+7+6,,,1)
def my_funct(n):
    if n == 1:
        # if the values get 1==1 call it will start returning values till n+n-1
        return 1
    return n + my_funct(n - 1)
x = my_funct(10)
print(x)