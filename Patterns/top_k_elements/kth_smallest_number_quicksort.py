'''
Find the kth smallest number using Quick sort technique - also known as Quick select
https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/?ref=leftbar-rightbar
'''


def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1


def quicksort(arr, low, high, K):
    if low < high:
        pivot = partition(arr, low, high)
        if pivot == K-1:
            return pivot
        quicksort(arr, low, pivot-1, K)
        quicksort(arr, pivot+1, high, K)


arr = [5, 12, 11, -1, 12]
pivot = quicksort(arr, 0, len(arr)-1, 3)
print(arr[pivot])
