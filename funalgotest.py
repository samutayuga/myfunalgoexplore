class MyAlgoForFun:
    """
    This is reverse with O(n) linear running time and constant memory complexity
    The problem is that we want to reverse a T[] array in O(N) linear time complexity
    and we want the algorithm to be in-place as well - so no additional memory can be used!
    For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]
    """

    def reverse(self, nums):
        # pointer to the left most
        left_most = 0
        # pointer to the right most
        right_most = len(nums) - 1
        # The algo will run as long as the right most
        # is greater than the left most pointer
        # no additional array is introduced
        while right_most > left_most:
            # 1. swap the value between element at 0 and n-1, where n-1 is the len of the array
            nums[left_most], nums[right_most] = nums[right_most], nums[left_most]
            # 2. move the left and right pointer so that they are getting closer every time until they collide
            # Once they collide means the algo will stop
            right_most = right_most - 1
            left_most = left_most + 1

        return nums

    """
    A palindrome is a string that reads the same forward and backward"
    For example: radar or madam
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
    Our task is to design an efficient algorithm to reverse a given integer. 
    For example if the input of the algorithm is 1234 then the output should be 4321.
    """

    def reverse_integer(self, aNumber):
        revesed = 0
        n = aNumber
        while n > 0:
            remainder = n % 10
            n = n // 10
            revesed = revesed * 10 + remainder
        return revesed

    """
    Construct an algorithm to check whether two words (or phrases) are anagrams or not!
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once
    For example: restful and fluster
    """

    def is_anagram(self, str1, str2):
        # if the len is different then str1 and str2 is not anagram
        if len(str1) != len(str2):
            return False
        # sort
        # this is bottleneck because it has O(NlogN)
        str1 = sorted(str1)
        str2 = sorted(str2)

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        # overall running time complexity os O(NlogN)+O(N) = O(NlogN)
        return True

    """
    The problem is that we want to sort a 
    T[] one-dimensional array of integers in O(N) 
    running time - and without any extra memory. 
    The array can contain values: 0, 1 and 2 (check out the theoretical 
    section for further information).
    eg, [0,2,2,2,2,2,2,1,0,0,0,6]
    """

    def dutch_flag(self, nums, pivot=1):
        # the pointer to track the 0 value, it is initialized with 0 value, means it is in the beginning
        # of the array
        i = 0
        # the pointer to track the 2 value, it is initialized with the last index, means it is assumed in the last
        # of the array
        k = len(nums) - 1
        # the pointer to track the 1 value, it is initialized with 0 value, means it is assumed in the beginning
        # of the array
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
