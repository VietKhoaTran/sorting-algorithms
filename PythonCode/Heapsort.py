def heapify(arr, n, i):
    largest = i 
    l = 2*i +1
    r = 2*i +2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    for i in range(len(arr)//2 -1, -1, -1):
        heapify(arr, len(arr), i)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

arr = [1,4,3,2,9,10,7,4,8,6]
heapSort(arr)
print(arr)