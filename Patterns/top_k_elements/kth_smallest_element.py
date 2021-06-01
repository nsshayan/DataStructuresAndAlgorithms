'''
https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/?ref=leftbar-rightbar
K’th Smallest/Largest Element in Unsorted Array
Using Max_heap the complexity is O(NlogK)
Using Min_heap the complexity is O(KlogN)
'''

from heapq import *


def find_kth_smallest_number(arr, k):
    max_heap = []

    for i in range(k):
        heappush(max_heap, -arr[i])

    for i in range(k, len(arr)):
        if arr[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -arr[i])

    return -max_heap[0]


print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3))
print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4))
print(find_kth_smallest_number([5, 12, 11, -1, 12], 3))
