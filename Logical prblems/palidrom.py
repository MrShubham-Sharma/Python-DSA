# to check wherther the number is palidrome or not 
n=1234 
num =n
# for the initia result
result =0
while num >0:
    # to extract the last digit we use % 10
    last_digit=num %10

    # result where we convert the number in reverse order  
    result=(result*10)+last_digit 
    # // for the single digit division 
    num = num//10
    print(n==result)

# timecomplexity is o(log10(N))