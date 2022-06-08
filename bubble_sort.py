class BubbleSort:
    def __init__(self, nums):
        self.nums = nums

    def sort(self, ascending=True):
        """
        [-10,1,1000,-9]
        :return:
        """
        for i in range(len(self.nums) - 1):
            for j in range(len(self.nums) - i - 1):
                if ascending:
                    if self.nums[j] > self.nums[j + 1]:
                        self.swap(j, j + 1)
                else:
                    if self.nums[j] < self.nums[j + 1]:
                        self.swap(j, j + 1)

    def swap(self, j, k):
        """
        :param j:
        :param k:
        :return:
        """
        self.nums[j], self.nums[k] = self.nums[k], self.nums[j]
