from random import randint, uniform
from random_words import RandomWords
from numpy import mean
from time import time

int_list = [randint(0, 1000) for i in range(5000)]
float_list = [uniform(0.1, 100.0) for i in range(5000)]
word = RandomWords()
str_list = [word.random_word() for i in range(5000)]


def heapify(nums, heap_size, root_index):
	# Assume the index of the largest element is the root index
	largest = root_index
	left_child = (2 * root_index) + 1
	right_child = (2 * root_index) + 2

	# If the left child of the root is a valid index, and the element is greater
	# than the current largest element, then update the largest element
	if left_child < heap_size and nums[left_child] > nums[largest]:
		largest = left_child

	# Do the same for the right child of the root
	if right_child < heap_size and nums[right_child] > nums[largest]:
		largest = right_child

	# If the largest element is no longer the root element, swap them
	if largest != root_index:
		nums[root_index], nums[largest] = nums[largest], nums[root_index]
		# Heapify the new root element to ensure it's the largest
		heapify(nums, heap_size, largest)


def heap_sort(nums):
	n = len(nums)

	# Create a Max Heap from the list
	# The 2nd argument of range means we stop at the element before -1 i.e.
	# the first element of the list.
	# The 3rd argument of range means we iterate backwards, reducing the count
	# of i by 1
	for i in range(n, -1, -1):
		heapify(nums, n, i)

	# Move the root of the max heap to the end of
	for i in range(n - 1, 0, -1):
		nums[i], nums[0] = nums[0], nums[i]
		heapify(nums, i, 0)


def mean_time(lst, iterations):
	sort_dur_list = []
	for loop in range(iterations):
		start_time = time()
		heap_sort(lst)
		duration = time() - start_time
		sort_dur_list.append(duration)
	return mean(sort_dur_list)


int_time_mean = mean_time(int_list, 10)
float_time_mean = mean_time(float_list, 10)
word_time_mean = mean_time(str_list, 10)

# print(int_time_mean)
# print(float_time_mean)
# print(word_time_mean)
