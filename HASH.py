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
# we doesn't used an extra space so SC is O(1)