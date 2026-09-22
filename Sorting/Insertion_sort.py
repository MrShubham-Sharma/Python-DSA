def insertion_sort(nums):
    n = len(nums)
    
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        
        # Shift elements of nums[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
            
        # Place key at its correct position
        nums[j + 1] = key


# Test the code with the array from the image:
nums = [3, 4, 5, 6, 8, 9, 10, 7, 1]

print("Original array:", nums)
insertion_sort(nums)
print("Sorted array:  ", nums)