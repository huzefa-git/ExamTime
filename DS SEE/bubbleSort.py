arr = [int(x) for x in input("Enter elements:").split()]
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
print("The sorted array is:",arr)