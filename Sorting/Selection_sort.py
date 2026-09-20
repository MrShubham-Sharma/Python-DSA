def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            # Use square brackets for indexing list elements
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap the smallest found element with the current position i
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

# Input list
num_list = [2, 24, 6, 7, 5, 1, 3, 8, 9]

# Call function and print result
sorted_list = selection_sort(num_list)
print(sorted_list)

def decending_sort(num):
    n=len(num)
    for i in range(0,n):
        max_index=i
        for j in range(i+1,n):
            if num[j]>num[max_index]:
                max_index=j
        num[i],num[max_index]=num[max_index],num[i]
    return num
num_list=[1,3,5,8,9,6,7]
sorted_list=decending_sort(num_list)
print(sorted_list)