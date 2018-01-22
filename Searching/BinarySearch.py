def binarySearch(arr, l, r, x):
    if r >=1:
        mid = l + (r -1) / 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1,x)
        else:
            return binarySearch(arr, mid+1,r, x)
    else:

arr = [2,3,7,45,5]
x = 10

result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
     print "Element is present at index %d" % result
else:
    print "Element is not present in array"