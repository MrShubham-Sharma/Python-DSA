# Reverse array by Recursion 
nums = [2, 4, 1, 7, 6, 3, 8, 9, 5]
def func(nums, left, right):
    # Base case: stop when left pointer crosses or meets right pointer
    if left >= right:
        return

    # Swap elements at left and right indices
    nums[left], nums[right] = nums[right], nums[left]

    # Recursive call moving both pointers inward
    func(nums, left + 1, right - 1)


def reverseArray(nums, l, r):
    func(nums, l, r)
    return nums

reverseArray(nums, 0, len(nums) - 1)
print(nums)