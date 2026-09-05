# check the frequency of each number and save in dictionary according to the frequency 
n = [1,2,4,5,3,3,5,3,5,5,6,6,7,7]
my_dict ={}
# Method 1
for i in range(0,len(n)):
    # TC will be O(n) for the itrrations are woking Nth times 
    if n[i] in my_dict:
        # TC will be the O(1) for the updating number 
        # it will itrrate the number if exist in dict then add +1 likewise {5:3}
        my_dict[n[i]] += 1
    else:
        # TC will be the O(1) for the updating number 
        # it will add on the number if not extst like {1:1}
        my_dict[n[i]] = 1
print(my_dict)

# Method 2 
for i in range(0,len(n)):
    my_dict[n[i]]=my_dict.get(n[i],0)+1
    #  with this it will gives an same evaluation like wise
    #  my_dict[5]= my_dict.get(n[5],0) it will retun the values like if not 
    #  exist then it will return the values like 0+1 = {5:1}
    # if exist then it will add on simply {5:3}
print(my_dict)