
def maxHeapify(arr,i,N):
    left = 2 * i
    right = 2 * i + 1
    
    if left <= N and arr[left-1] > arr[i-1]:
        largest = left
    else :
        largest = i
    
    if right <= N and arr[right-1] > arr[largest-1]:
        largest = right
    
    if largest != i:
       #swap(arr[i-1],arr[largest-1])
        temp = arr[i-1]
        arr[i-1]=arr[largest-1]
        arr[largest-1]=temp
        maxHeapify(arr, largest, N)



