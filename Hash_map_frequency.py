# check the frequency of each number and save in dictionary according to the frequency 
n = [1,2,4,5,3,3,5,3,5,5,6,6,7,7]
my_dict ={}
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
