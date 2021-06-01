

def mergesort(arr):
    if len(arr) > 1:

         # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergesort(L)

        # Sorting the second half
        mergesort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Code to print the list


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
mergesort(arr)
print(arr)

'''
def merge(arr, l, m, r):
    i = l
    j = m
    left = arr[:m]
    right = arr[m:]
    k = l
    while i < m and j < r:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < m:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < r:
        arr[k] = right[j]
        k += 1
        j += 1


def mergesort(arr, l, r):
    m = (l+r)//2
    mergesort(arr, l, m)
    mergesort(arr, m+1, r)

    merge(arr, l, m, r)

'''
