class MyAlgoForFun:
    """
    This is reverse with O(n) linear running time and constant memory complexity
    """

    def reverse(self, nums):
        # pointer
        left_most = 0
        right_most = len(nums) - 1
        while right_most > left_most:
            nums[left_most], nums[right_most] = nums[right_most], nums[left_most]
            right_most = right_most - 1
            left_most = left_most + 1

        return nums

    """
        This is reverse with O(n) linear running time and constant memory complexity
        """

    def is_polindrom(self, data):
        x = list(data)
        x = self.reverse(x)
        y = "".join(x)
        if y == data:
            return True
        return False

    """
    Reverse the integer, eg. 1234567891
    With the O(n) running time complexity
    """

    def reverse_integer(self, aNumber):
        module = 0
        revesed = 0
        n = aNumber
        while n > 0:
            remainder = n % 10
            n = n // 10
            revesed = revesed * 10 + remainder
        return revesed

    """
    Sorting an array with 3 distinct known values
    eg, [0,2,2,2,2,2,2,1,0,0,0,6]
    """

    def dutch_flag(self, nums, pivot=1):
        i = 0
        k = len(nums) - 1
        j = 0
        while j <= k:
            # check if j
            if nums[j] < pivot:
                # swap num[j] with nums[i] increment j by 1
                nums[j], nums[i] = nums[i], nums[j]
                j = j + 1
                i = i + 1
            elif nums[j] > pivot:
                # swap num[j] with nums[k] decrement k by 1
                nums[j], nums[k] = nums[k], nums[j]
                k = k - 1
            else:
                j = j + 1
        return nums
