# brute force
n = [2,4,5,6,7,8,4.6,4,5,6]
m =[2,3,4,6,7]
# we have to count how many times each number was repeted 
for num in m:
    count =0
    for x in n :
        if x==num:
            count+=1
    print(count)
# it's an nested loop so it's TC is O(n*m)
# it's an N*M because the both are dependent on each other  

# we doesn't used an extra space so SC is O(1)

# optimal solution 

o=[2,3,4,4,2,2,4,5,6,10]
p= [1,3,5,34,6,4,2,10]
# we are going for the ahshing where we presotre the elements like 
# as an notebook 
hash_list = [0]*11
for number in o:
    hash_list[number]+=1
    for z in p :
        # it will allow the numbers between 1-10
        if z <1 or z>10:
            print(0)
        else:
            print(hash_list[number])
# in this loop the both loops are working on hashing storage so it's an 
# TC O(N+M)
# and SC is O(11) cause of using an 11 index where 11 is an constant value
#  so we can assume it as O(1)

# by using an dictionary 

# as per hasing we created prestorage
my_dict ={}

for num in n:
    # we use the logic if the number in the dictionary it will count 
    # if not it will return 0
    my_dict[num]=my_dict.get(num,0)+1
for x in m:
    if x in my_dict:
        print(my_dict[x])
    else:
        print(0)

# TC and SC will be same 