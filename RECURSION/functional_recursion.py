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