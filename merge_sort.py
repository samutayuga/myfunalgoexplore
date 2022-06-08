def merge_sort(nums):
    if len(nums) == 1:
        return
    # divide into 2
    middle_indx = len(nums) // 2
    half_left = nums[:middle_indx]
    half_right = nums[middle_indx:]

    merge_sort(half_left)
    merge_sort(half_right)

    # new data structure
    # merge_arr = [0 for _ in range(0, len(half_left) + len(half_right))]
    # conqueror

    i, j, k = 0, 0, 0

    while i < len(half_left) and j < len(half_right):
        if half_left[i] < half_right[j]:
            nums[k] = half_left[i]
            i += 1
        else:
            nums[k] = half_right[j]
            j += 1

        k += 1

        # additional item in either left or right sub array

        # if len(half_left) > len(half_right):
        # just copy remaining of left sub array into merge array
    while i < len(half_left):
        nums[k] = half_left[i]
        k += 1
        i += 1

    # if len(half_right) > len(half_left):
    # just copy remaining of left sub array into merge array
    while j < len(half_right):
        nums[k] = half_right[j]
        k += 1
        j += 1
    return nums
