def optimized_bubble_sort(nums):
    n = len(nums)

    for i in range(n - 2, -1, -1):
        is_swapped = False  # Reset flag before each pass

        for j in range(0, i + 1):
            # Check if adjacent elements need swapping
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swapped = True  # A swap occurred!

        print(f"   Array after pass: {nums}")

        # If no elements were swapped during this pass, array is sorted
        if not is_swapped:
            break
        
    return nums

# Example test array
numbers = [5, 1, 6, 8, 2, 9, 4]
sorted_numbers = optimized_bubble_sort(numbers)
print(sorted_numbers)