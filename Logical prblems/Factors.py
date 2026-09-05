# brute force
n =36
num =n
result = []
for i in range(1,num+1):
    # in this case we're going to all of the itrrassion
    if num % i ==0:
    # it give the result as reminder if 1% 36 = 36, 6%36 = 6 
        result.append(i)
print(result)
# time complexity is O(N)
# space complexity is O(K)



# better solution
number =25
result =[]
# we found the facotrs are often in the half part after that the number himself is a factor
# so insted of going to whole itrration we just go for half part
for i in range(1,number//2):
    if number % i ==0:
        result.append(i)

# in last we added the number himself as an factor
result.append(number)
print(result)

# we have use the the time complexity of O(N/2)
# and sapce complexity as O(K) K because it's depend on the factors 

# optimal solution
from math import sqrt 
a = 48 
result =[]

# in this case we identify the sqrt is also the factor so we go till half
# likewise 1,2,4,6,8,12....48
for i in range(1,int(sqrt(a))+1):
    if a % i==0:
        result.append(i)
    # we can get the problem like 6,6 as sqrt and number himself so solution
    if a// i !=i:
        result.append(a//i)
    # if we want the in order 
    result.sort()
print(result)

# time complexity is O(sqrt(N))+O(NlogN)
# SC is O(K)