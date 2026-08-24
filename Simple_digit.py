# for extract the single digit values input from 54743

n= 54743
num =n 
while num>0:
    last_digit =num % 10
    # it will give the reminder
    print(last_digit)
    # it will convert the floor division in integer value
    num =num // 10
