arr = [int(x) for x in input("Enter elements:").split()]
for i in range(len(arr)):
    index = i
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[index]):
            index = j
    arr[i],arr[index] = arr[index],arr[i]
print("The sorted array is:",arr)