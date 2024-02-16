arr = [12,23,34,45,55,62,71,85,96]
key = 96
c=0
for i in range(len(arr)):
    if(arr[i]==key):
        c+=1
if(c==1):
    print("found at",i)
else:
    print("Not found")