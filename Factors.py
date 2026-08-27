# brute force
n =36
num =n
result = []
for i in range(1,num+1):
    if num % i ==0:
        result.append(i)
print(result)

# better solution
number =25
result =[]
for i in range(1,number//2):
    if number % i ==0:
        result.append(i)
result.append(number)
print(result)