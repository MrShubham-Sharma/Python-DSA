def merge_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2
    
    # Recursively split and sort the left and right halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the two sorted halves together
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0  # Indexes for tracking positions in left and right arrays

    # Compare elements from both lists and append the smaller one to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements left over in left or right sub-arrays
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))