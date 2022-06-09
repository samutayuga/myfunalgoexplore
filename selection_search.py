def selection_sort(nums):
    # we make N-1 iteration
    for i in range(len(nums) - 1):
        # linear search and the index stores the index
        # of the min item
        index = i
        # This is the linear search
        for j in range(i, len(nums)):
            """
            [5,4,3,1,-1,10]
            """
            if nums[j] < nums[index]:
                index = j
        # we have to swap the min item with item in the last
        # we do not swap the item with itself

        if index != i:
            nums[index], nums[i] = nums[i], nums[index]
    return nums
