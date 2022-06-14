class QuickSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        self.quick_sort(0, len(self.data) - 1)

    def quick_sort(self, low, high):
        if low >= high:
            return
        pivot_index = self.partition(low, high)
        # call the function recursively on the left sub array
        self.quick_sort(low, pivot_index - 1)
        # call the funciton recursively on the right sub array
        self.quick_sort(pivot_index + 1, high)

    # this is where the magic began
    def partition(self, low, high):
        # we use the middle item as the pivot
        pivot_index = (low + high) // 2
        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]
        # consider all the other items and compare them with the pivot
        for j in range(low, high):
            if self.data[j] <= self.data[high]:
                self.data[low], self.data[j] = self.data[j], self.data[low]
                low = low + 1
        # we have considered all items then swap the high and low
        self.data[low], self.data[high] = self.data[high], self.data[low]
        return low
