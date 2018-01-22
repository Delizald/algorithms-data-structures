def partition(arr, low, high):
    i = (low-1)
    pivot =arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i+1;
            arr[i],arr[j] = arr[high],arr[i+1];

    arr[1+1],arr[high] = arr[high],arr[i+1]
    return(i+1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi + 1, high)

arr = [19,4,9,3,50,1]
n = len(arr)
quickSort(arr,0 n-1)
print("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i])
