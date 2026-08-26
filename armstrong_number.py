# to create code for check the number is armstrong or not 
n=153
num =n 
total =0

# for the power of the string like wise 1^3
number_of_digit =len(str(n))
while num >0:
    last_digit = num %10

    # logit is 3+5^3
    total = total+last_digit** number_of_digit
    num = num //10
    print(total)

# check where number is amstrong or not 
print(total==n)
