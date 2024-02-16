def binarySearch(arr,low,high,key):
    mid=(low+high)//2
    if(arr[mid])==key:
        print("Found at",mid)
    else:
        if(key<arr[mid]):
            mid = high-1
        else:
            mid = low+1
arr = [int(x) for x in input("Enter elements:").split()]
key=int(input("Enter the key:"))
low = 0
high = len(arr)-1
binarySearch(arr,low,high,key)