class Person:
    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return str(self.name)


def sort_person(persons, ascending=True):
    for idx in range(len(persons)):
        minAgeidx = idx
        if ascending:
            while minAgeidx > 0 and persons[minAgeidx - 1] > persons[minAgeidx]:
                persons[minAgeidx - 1], persons[minAgeidx] = persons[minAgeidx], persons[minAgeidx - 1]
                minAgeidx -= 1
    return persons


def insertion_sort(nums, ascending=True):
    for i in range(len(nums)):
        j = i
        # check all the preceding
        # items if it is greater than the current item
        # until found the one that is smaller or stop
        # when all are compared
        if ascending:
            while j > 0 and nums[j - 1] > nums[j]:
                # swap to previous index
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
        else:
            while j > 0 and nums[j - 1] < nums[j]:
                # swap to previous index
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
    return nums


def shell_sort(nums, ascending=True):
    gap = len(nums) // 2
    while gap > 0:
        for i in range(len(nums)):
            j = i
            if ascending:
                while j > 0 and nums[j - gap] > nums[j]:
                    # swap
                    nums[j - gap], nums[j] = nums[j], nums[j - gap]
                    j = j - gap

        gap = gap // 2
