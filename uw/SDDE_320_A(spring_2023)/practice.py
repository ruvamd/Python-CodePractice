import heapq

class StreamingMedianCalculator:
    def __init__(self, initial_values):
        self.min_heap = []  # min heap for the larger half of the values
        self.max_heap = []  # max heap for the smaller half of the values
        for value in initial_values:
            self.add_number(value)

    def add_number_and_return_median(self, value):
        self.add_number(value)
        return self.get_median()

    def add_number(self, value):
        if len(self.min_heap) == len(self.max_heap):
            # if both heaps have the same size, add the value to the max heap
            if len(self.min_heap) > 0 and value > self.min_heap[0]:
                # if the value is greater than the smallest value in the min heap,
                # move the smallest value to the max heap
                smallest_min_heap = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -smallest_min_heap)
            heapq.heappush(self.max_heap, -value)
        else:
            # if the max heap has one more element than the min heap,
            # add the value to the min heap
            if value < -self.max_heap[0]:
                # if the value is smaller than the largest value in the max heap,
                # move the largest value to the min heap
                largest_max_heap = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, largest_max_heap)
            heapq.heappush(self.min_heap, value)

    def get_median(self):
        if len(self.min_heap) == len(self.max_heap):
            # if both heaps have the same size, the median is the average of the
            # smallest value in the min heap and the largest value in the max heap
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            # if the max heap has one more element than the min heap,
            # the median is the largest value in the max heap
            return -self.max_heap[0]

# create a new StreamingMedianCalculator object with initial values
a = StreamingMedianCalculator([1, 16, 7, 9, 14, 27, 34, 15, 61, 43, 52])

# add a new value and get the updated median
median1 = a.add_number_and_return_median(11)
print(median1)  # output: 13.5

# add another new value and get the updated median
median2 = a.add_number_and_return_median(22)
print(median2)  # output: 22

# add yet another new value and get the updated median
median3 = a.add_number_and_return_median(15)
print(median3)  # output: 15.5