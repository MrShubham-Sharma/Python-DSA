# for extract the single digit values input from 54743

n= 54743
num =n 
while num>0:
    last_digit =num % 10
    # it will give the reminder
    print(last_digit)
    # it will convert the floor division in integer value
    num =num // 10
# for the count the numbers in form of loop approch and the log approch 
n =284439
num =n 
count =0
while num >0:
    count+=1
    num = num //10
print(count)

from math import log10

def count_digit(n):
    return int(log10(n)) + 1

print(count_digit(284439))